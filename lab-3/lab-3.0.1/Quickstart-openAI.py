import os  
import base64
from openai import AzureOpenAI  

endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-35-turbo")  
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "da7b94fbdda046fa921c4f19415ed8fe")  

# Initialize Azure OpenAI Service client with key-based authentication    
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version="2025-01-01-preview",
)
    
    

#Prepare the chat prompt 
chat_prompt = [
    {
        "role": "user",
        "content": "Que es Azure OpenAI Service?"
    }
   
] 
    
# Include speech result if speech is enabled  
messages = chat_prompt  
    
# respon the completion  
completion = client.chat.completions.create(  
    model=deployment,
    messages=messages,
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=True 
)


for update in completion:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")    

client.close()