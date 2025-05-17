# https://learn.microsoft.com/en-us/azure/ai-services/translator/document-translation/quickstarts/client-library-sdks?tabs=dotnet&pivots=programming-language-python

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import SingleDocumentTranslationClient
from azure.ai.translation.document.models import DocumentTranslateContent


def sample_single_document_translation():

    # create variables for your resource api key, document translation endpoint, and target language
    key = "F4d29sI6e8UZ6q7hSFQrqS2irm2aNpfqe4RAlfBbCeZ4r2URlmz5JQQJ99BDACYeBjFXJ3w3AAAbACOGT5KE"
    endpoint = "https://translatorfabrik.cognitiveservices.azure.com/translator"
    target_language = "es"

    # initialize a new instance of the SingleDocumentTranslationClient object to interact with the synchronous Document translation feature
    client = SingleDocumentTranslationClient(endpoint, AzureKeyCredential(key))

    # absolute path to your document
    file_path = "C:/Users/RonalGonzalez/Pictures/hand-on-labs-AI-102/lab-2/lab-2.0.4/document-translation-sample.docx"
    file_name = os.path.basename(file_path)
    file_type = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    print(f"File for translation: {file_name}")

    with open(file_path, "rb") as file:
        file_contents = file.read()

    document_content = (file_name, file_contents, file_type)
    document_translate_content = DocumentTranslateContent(document=document_content)

    response_stream = client.document_translate(
        body=document_translate_content, target_language=target_language
    )
    # Save the response_stream to a file
    output_file_path = "./translated-document.docx"
    with open(output_file_path, "wb") as output_file:
        output_file.write(response_stream)
    
    print(f"Translated document saved to: {output_file_path}")


if __name__ == "__main__":
    sample_single_document_translation()