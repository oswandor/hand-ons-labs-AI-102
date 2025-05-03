import requests
import os

location = os.getenv("VIDEO_INDEXER_LOCATION", "trial")  # Cambia según tu región
account_id = os.getenv("VIDEO_INDEXER_ACCOUNT_ID")  # Cambia según tu cuenta
subscription_key = os.getenv("VIDEO_INDEXER_SUBSCRIPTION_KEY")  # Cambia según tu clave de suscripción

access_token = os.getenv("VIDEO_INDEXER_ACCESS_TOKEN")
video_id = os.getenv("VIDEO_INDEXER_VIDEO_ID")  # ID del video que deseas verificar

# Verificar el estado del video
status_url = f"https://api.videoindexer.ai/{location}/Accounts/{account_id}/Videos/{video_id}/Index?accessToken={access_token}"

response = requests.get(status_url)
status = response.json()["state"]
print("Estado del video:", status)  # "Processed" cuando termine


# Obtener los insights del video
# Asegúrate de que el video esté procesado antes de intentar obtener insights
insights_url = f"https://api.videoindexer.ai/{location}/Accounts/{account_id}/Videos/{video_id}/Index?accessToken={access_token}"

response = requests.get(insights_url)
insights = response.json()


# Extracción de datos específicos
def get_insights(insights):

    # 1. Transcripción (si existe)
    transcript = insights["videos"][0]["insights"]["transcript"]
    print("\n--- Transcripción ---")
    for line in transcript:
        if line["text"].strip():  # Ignorar líneas vacías
            print(f"Texto: {line['text']} (Confianza: {line['confidence']:.2f})")

    # 2. Sentimientos (emociones)
    print("\n--- Sentimientos ---")
    sentiments = insights["summarizedInsights"]["sentiments"]
    for sentiment in sentiments:
        print(f"Tipo: {sentiment['sentimentKey']} - Duración: {sentiment['seenDurationRatio']*100:.1f}%")

    # 3. Caras detectadas (si hay)
    faces = insights["summarizedInsights"]["faces"]
    if faces:
        print("\n--- Caras ---")
        for face in faces:
            print(f"ID: {face['id']}, Género: {face['gender']}, Edad: {face['age']}")
    else:
        print("\nNo se detectaron caras.")

    # 4. Palabras clave (keywords)
    keywords = insights["summarizedInsights"]["keywords"]
    if keywords:
        print("\n--- Palabras Clave ---")
        for kw in keywords:
            print(f"Keyword: {kw['name']} (Appears {len(kw['appearances'])} veces)")
    else:
        print("\nNo se detectaron palabras clave.")

    detectedObjects = insights["videos"][0]["insights"]["detectedObjects"]

    if detectedObjects:
        print("\n--- Objetos Detectados ---")
        for obj in detectedObjects:
            print(f"Objeto: {obj['displayName']}")
    else:
        print("\nNo se detectaron objetos.")

        

    # 5. Estadísticas (ejemplo)
    stats = insights["summarizedInsights"]["statistics"]
    print("\n--- Estadísticas ---")
    print(f"Correspondencias: {stats['correspondenceCount']}")


get_insights(insights)
