from azure.identity import ClientSecretCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Configuración
tenant_id = ""  # Obtener con: az account show --query tenantId -o tsv
client_id = ""        # El appId obtenido anteriormente
client_secret = ""   # La contraseña generada

# Autenticación
credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

# Crear cliente (ejemplo con Text Analytics)
client = TextAnalyticsClient(
    endpoint="https://handsonlabsai102.cognitiveservices.azure.com/",
    credential=credential
)

TextAnalyticsClient()

# Probar el servicio
documents = ["Este es un texto de prueba para Azure Cognitive Services"]
result = client.analyze_sentiment(documents)
print(result[0].sentiment)