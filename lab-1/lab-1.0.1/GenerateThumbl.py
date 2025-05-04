# Documentacion  https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/how-to/generate-thumbnail


import requests
import matplotlib.pyplot as plt
from PIL import Image
import io
import os

# Configuración
endpoint = os.getenv("AZURE_VISION_ENDPOINT", "https://your-default-endpoint.cognitiveservices.azure.com/vision/v3.2/generateThumbnail")
api_key = os.getenv("AZURE_VISION_API_KEY", "your-default-api-key")

params = {
    "width": 100,
    "height": 100,
    "smartCropping": "true"
}
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json"
}
body = {
    "url": "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"
}

# Llamar a la API
response = requests.post(
    url=endpoint,
    params=params,
    headers=headers,
    json=body
)

# Procesar respuesta
if response.status_code == 200:
    output_path = "thumbnail_smart_crop.jpg"
    with open(output_path, "wb") as f:
        f.write(response.content)
    
    print(f"✅ Thumbnail guardado en: {output_path}")
    img = Image.open(output_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
else:
    print(f"❌ Error {response.status_code}: {response.text}")