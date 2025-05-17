

from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError

# set `<your-key>`, `<your-endpoint>`, and  `<region>` variables with the values from the Azure portal
key = "F4d29sI6e8UZ6q7hSFQrqS2irm2aNpfqe4RAlfBbCeZ4r2URlmz5JQQJ99BDACYeBjFXJ3w3AAAbACOGT5KE"
endpoint = "https://api.cognitive.microsofttranslator.com/"
region = "eastus"

credential = TranslatorCredential(key, region)
text_translator = TextTranslationClient(endpoint=endpoint, credential=credential)

try:
    source_language = "en"
    target_languages = ["es", "it"]
    input_text_elements = [ InputTextItem(text = "This is a test") ]

    response = text_translator.translate(content = input_text_elements, to = target_languages, from_parameter = source_language)
    translation = response[0] if response else None

    if translation:
        for translated_text in translation.translations:
            print(f"Text was translated to: '{translated_text.to}' and the result is: '{translated_text.text}'.")

except HttpResponseError as exception:
    print(f"Error Code: {exception.error.code}")
    print(f"Message: {exception.error.message}")