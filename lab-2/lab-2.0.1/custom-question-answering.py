# Documentacion https://learn.microsoft.com/en-us/azure/ai-services/language-service/question-answering/quickstart/sdk?tabs=windows&pivots=rest 

import os 
import requests
import json
# This example requires environment variables named "LANGUAGE_KEY" and "LANGUAGE_ENDPOINT"

api_key = "9Vaeh6fqDa1qVjnb9lZggwH1mYWegfgVJmxqr2Ubl9imtjHotUZMJQQJ99BCACYeBjFXJ3w3AAAaACOG2nye" 
api_endpoint = "https://lang-serverless-prod-eastus.cognitiveservices.azure.com/"
PROJECT_NAME = "Questionproject"
DEPLOYMENT_NAME = "production"


# https://lang-serverless-prod-eastus.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=Questionproject&api-version=2021-10-01&deploymentName=production
# Construir la URL para la petición
url = f"{api_endpoint}language/:query-knowledgebases"

# Parámetros de consulta
params = {
    "projectName": PROJECT_NAME,
    "api-version": "2021-10-01",
    "deploymentName": DEPLOYMENT_NAME
}

# Encabezados para la petición
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json"
}

# Datos para la petición
data = {
    "question": "How much battery life do I have left?"
}

# Realizar la petición POST
try:
    response = requests.post(url, headers=headers, params=params, json=data)
    response.raise_for_status()  # Lanzar excepción para códigos de error HTTP
    
    # Mostrar la respuesta
    result = response.json()
    print("Respuesta:")
    print(json.dumps(result, indent=2))
    
except requests.exceptions.HTTPError as e:
    print(f"Error en la petición HTTP: {e}")
    print(f"Respuesta del servidor: {response.text}")
except Exception as e:
    print(f"Error: {e}")