
# List all subscriptions
az account list  --output table

# Set the subscription to the one you want to use
az account set --subscription "71fa9946-b620-4f31-a39f-0d00a0efa5f2"

# Create a resource account OpenAI
az cognitiveservices account create \
-n $(uuidgen | tr '[:upper:]' '[:lower:]' | cut -c1-20) \
-g rg-fabrikai102 \
-l eastus \
--kind OpenAI \
--sku s0 \
--subscription 71fa9946-b620-4f31-a39f-0d00a0efa5f2

# Create a resource account OpenAI with the name MyOpenAIResource
az cognitiveservices account deployment create \
   -g rg-handonslabs \
   -n cognitiveservicefabrik \
   --deployment-name gpt-35-turbo \
   --model-name gpt-35-turbo \
   --model-version "0125"  \
   --model-format OpenAI \
   --sku-name "Standard" \
   --sku-capacity 1


{
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are an AI assistant that helps people find information."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Hola"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "¡Hola! ¿Cómo puedo ayudarte hoy? 😊"
        }
      ]
    }
  ],
  "temperature": 0.7,
  "top_p": 0.95,
  "max_tokens": 800
}

   curl "https://cognitiveservicefabrik.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2025-01-01-preview" \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d "$payload"
   