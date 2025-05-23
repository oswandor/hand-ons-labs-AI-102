# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""
DESCRIPTION:
    This sample demonstrates how to detect physical objects in an image file sample.jpg, using a synchronous client.

    The synchronous (blocking) `analyze` method call returns an `ImageAnalysisResult` object.
    Its `objects` property (a `ObjectsResult` object) contains a list of `DetectedObject` objects. Each has:
    - The object name, for example: "chair", "laptop". 
    - A confidence score in the range [0, 1], with higher values indicating greater confidences in the detection.
    - A `BoundingBox` coordinates in pixels, for a rectangular surrounding the object in the image.

    Object names are only supported in English at the moment.

USAGE:
    python sample_objects_image_file.py

    Set these two environment variables before running the sample:
    1) VISION_ENDPOINT - Your endpoint URL, in the form https://your-resource-name.cognitiveservices.azure.com
                         where `your-resource-name` is your unique Azure Computer Vision resource name.
    2) VISION_KEY - Your Computer Vision key (a 32-character Hexadecimal number)
"""


def sample_objects_image_file():
    import os
    from azure.ai.vision.imageanalysis import ImageAnalysisClient
    from azure.ai.vision.imageanalysis.models import VisualFeatures
    from azure.core.credentials import AzureKeyCredential
    from PIL import Image, ImageDraw, ImageFont
    import io
    import os 

    # Set the values of your computer vision endpoint and computer vision key
    # as environment variables:
    try:
        endpoint = os.getenv["VISION_ENDPOINT"]
        key = os.getenv["VISION_KEY"]
    except KeyError:
        print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
        print("Set them before running this sample.")
        exit()

    # Create an Image Analysis client
    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    # Ruta de la imagen a analizar
    image_path = "./sample.jpg"

    # Load image to analyze into a 'bytes' object
    with open(image_path, "rb") as f:
        image_data = f.read()

    # Detect objects in an image stream. This will be a synchronously (blocking) call.
    result = client.analyze(
        image_data=image_data,
        visual_features=[VisualFeatures.OBJECTS]
    )

    # Print Objects analysis results to the console
    print("Image analysis results:")
    print(" Objects:")
    if result.objects is not None:
        for object in result.objects.list:
            print(f"   '{object.tags[0].name}', {object.bounding_box}, Confidence: {object.tags[0].confidence:.4f}")
    print(f" Image height: {result.metadata.height}")
    print(f" Image width: {result.metadata.width}")
    print(f" Model version: {result.model_version}")


     # Crear una nueva imagen con cuadrados verdes alrededor de los objetos detectados
    # Abrir la imagen original
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    # Intentar cargar una fuente, o usar la fuente por defecto si no está disponible
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()

    # Dibujar cuadrados verdes alrededor de cada objeto detectado
    if result.objects is not None:
        for object in result.objects.list:
            # Obtener las coordenadas del cuadro delimitador
            x = object.bounding_box.x
            y = object.bounding_box.y
            w = object.bounding_box.width
            h = object.bounding_box.height
            
            # Dibujar un rectángulo verde
            draw.rectangle([(x, y), (x + w, y + h)], outline="red", width=3)
            
            # Añadir etiqueta con el nombre del objeto y la confianza
            label = f"{object.tags[0].name}: {object.tags[0].confidence:.2f}"
            draw.text((x, y-25), label, fill="red", font=font)

    # Guardar la nueva imagen
    output_path = "./sample_with_objects.jpg"
    # Por esto:
    image = image.convert('RGB')  # Convertir a modo RGB antes de guardar
    image.save(output_path)
    print(f"\nImagen con objetos marcados guardada en: {output_path}")




if __name__ == "__main__":
    sample_objects_image_file()