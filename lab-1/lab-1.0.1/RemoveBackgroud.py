# Documentacion  https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/how-to/background-removal

import requests
import os
from PIL import Image
from io import BytesIO

# Configura tus credenciales
endpoint = os.getenv("AZURE_ENDPOINT", "https://servicecongnitive.cognitiveservices.azure.com/")
api_key = os.getenv("AZURE_API_KEY", "your_default_api_key_here")

# URL de la API para eliminación de fondo
url = f"{endpoint}computervision/imageanalysis:segment?api-version=2023-02-01-preview&mode=backgroundRemoval"

# Cabeceras de la solicitud
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json"
}

# Opción 1: Usar una imagen remota (URL)
image_url = "https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/media/background-removal/building-1.png"
body = {"url": image_url}

# Opción 2: Usar una imagen local (cambiar a 'application/octet-stream')
# with open("tu_imagen.jpg", "rb") as f:
#     body = f.read()
# headers["Content-Type"] = "application/octet-stream"

# Enviar solicitud a la API
response = requests.post(url, headers=headers, json=body)

# Guardar el resultado (imagen PNG con fondo transparente)
if response.status_code == 200:
    output_path = "imagen_sin_fondo.png"
    with open(output_path, "wb") as f:
        f.write(response.content)
    print(f"✅ Imagen guardada en: {output_path}")
    
    # Mostrar la imagen (opcional)
    img = Image.open(output_path)
    img.show()
else:
    print(f"❌ Error {response.status_code}: {response.text}")