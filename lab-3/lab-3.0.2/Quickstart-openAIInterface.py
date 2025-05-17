from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
import os 

endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo")  
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")  

# https://eastus.api.cognitive.microsoft.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2025-01-01-preview
client = ChatCompletionsClient(endpoint=endpoint, credential=AzureKeyCredential(subscription_key),api_version="2024-06-01")

response = client.complete(
    stream=True,
    messages=[
        SystemMessage("You are a helpful assistant."),
        UserMessage("Give me 5 good reasons why I should exercise every day."),
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
)



for update in response:
    if update.choices and update.choices[0].delta:
        print(update.choices[0].delta.content or "", end="", flush=True)
    if update.usage:
        print(f"\n\nToken usage: {update.usage}")

client.close()