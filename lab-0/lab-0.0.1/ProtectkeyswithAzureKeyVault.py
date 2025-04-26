# Documentación 
# https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python?tabs=azure-cli

# Importación de las bibliotecas necesarias
import os
from azure.keyvault.secrets import SecretClient  # Cliente para manejar secretos en Azure Key Vault
from azure.identity import DefaultAzureCredential  # Para la autenticación con Azure

# Definición del nombre del Key Vault
keyVaultName = "keuvault-ai102labs"
# Construcción de la URL del Key Vault
KVUri = f"https://{keyVaultName}.vault.azure.net"

# Inicialización de las credenciales predeterminadas de Azure
credential = DefaultAzureCredential()
# Creación del cliente de secretos utilizando la URL del Key Vault y las credenciales
client = SecretClient(vault_url=KVUri, credential=credential)

# Nombre del secreto que queremos recuperar
secretName = "AISERVICEKEY"

print(f"Recuperando tu secreto desde {keyVaultName}.")

# Obtención del secreto desde Azure Key Vault
retrieved_secret = client.get_secret(secretName)

print(f"Tu secreto es '{retrieved_secret.value}'.")