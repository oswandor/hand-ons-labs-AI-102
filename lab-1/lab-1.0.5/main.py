import requests
import os

location = "trial"  # Cambia según tu región
account_id = os.getenv("VIDEO_INDEXER_ACCOUNT_ID")  # Configura esta variable de entorno
subscription_key = os.getenv("VIDEO_INDEXER_SUBSCRIPTION_KEY")  # Configura esta variable de entorno

# 1. Obtener token de acceso
auth_url = f"https://api.videoindexer.ai/auth/{location}/Accounts/{account_id}/AccessToken?allowEdit=true"
headers = {"Ocp-Apim-Subscription-Key": subscription_key}

response = requests.get(auth_url, headers=headers)
access_token = response.text.strip('"')  # El token viene entre comillas

print("Access Token:", access_token)


# Subir video a Video Indexer
file_path = "Bringing-AI-to-the-edge-Azure-Cognitive-Services.mp4"  # Ruta local del video

upload_url = f"https://api.videoindexer.ai/{location}/Accounts/{account_id}/Videos?accessToken={access_token}&name=MiVideo"

with open(file_path, "rb") as file:
    files = {"file": file}
    response = requests.post(upload_url, files=files)

video_id = response.json()["id"]
print("Video ID:", video_id)