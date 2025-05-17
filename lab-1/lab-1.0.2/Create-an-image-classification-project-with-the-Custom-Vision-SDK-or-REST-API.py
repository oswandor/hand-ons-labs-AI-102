# Documentacioni https://learn.microsoft.com/en-us/azure/ai-services/custom-vision-service/quickstarts/image-classification?tabs=linux%2Cvisual-studio&pivots=programming-language-python

# pip install azure-cognitiveservices-vision-customvision


from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid
import os

# Retrieve environment variables
ENDPOINT = os.getenv("CUSTOM_VISION_ENDPOINT")
training_key = os.getenv("CUSTOM_VISION_TRAINING_KEY")
prediction_key = os.getenv("CUSTOM_VISION_PREDICTION_KEY")
prediction_resource_id = os.getenv("CUSTOM_VISION_PREDICTION_RESOURCE_ID")

if not training_key or not prediction_key or not prediction_resource_id:
    raise ValueError("One or more environment variables are missing. Please set CUSTOM_VISION_TRAINING_KEY, CUSTOM_VISION_PREDICTION_KEY, and CUSTOM_VISION_PREDICTION_RESOURCE_ID.")

credentials = ApiKeyCredentials(in_headers={"Training-Key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-Key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)


publish_iteration_name = "classifyModel"

credentials = ApiKeyCredentials(in_headers={"Training-Key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# Create a new project
print ("Creating project...")
project_name = uuid.uuid4()
print("Project name: ", project_name)
project = trainer.create_project(project_name)



# Make two tags in the new project
hemlock_tag = trainer.create_tag(project.id, "Hemlock")
cherry_tag = trainer.create_tag(project.id, "Japanese Cherry")


base_image_location = os.path.join (os.path.dirname(__file__), "images")
print("Base image location: ", base_image_location)

print("Adding images...")

image_list = []

for image_num in range(1, 11):
    file_name = "hemlock_{}.jpg".format(image_num)
    with open(os.path.join (base_image_location, "Hemlock", file_name), "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[hemlock_tag.id]))

for image_num in range(1, 11):
    file_name = "japanese_cherry_{}.jpg".format(image_num)
    with open(os.path.join (base_image_location, "Japanese Cherry", file_name), "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[cherry_tag.id]))

upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=image_list))
if not upload_result.is_batch_successful:
    print("Image batch upload failed.")
    for image in upload_result.images:
        print("Image status: ", image.status)
    exit(-1)


print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    print ("Waiting 10 seconds...")
    time.sleep(10)

# The iteration is now trained. Publish it to the project endpoint
trainer.publish_iteration(project.id, iteration.id, publish_iteration_name, prediction_resource_id)
print ("Done!")


# Now there is a trained endpoint that can be used to make a prediction
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)


with open(os.path.join (base_image_location, "Test/test_image.jpg"), "rb") as image_contents:
    results = predictor.classify_image(
        project.id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))