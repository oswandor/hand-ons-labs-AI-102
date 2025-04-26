# Crear una nueva aplicación en Azure AD
app_id=$(az ad app create \
  --display-name "SP-Cognitive-FabrikAI" \
  --query appId --output tsv)

# Crear el Service Principal asociado
sp_id=$(az ad sp create --id $app_id --query id --output tsv)


# Asignar rol "Cognitive Services User" al grupo de recursos
az role assignment create \
  --assignee $sp_id \
  --role "Cognitive Services User" \
  --scope "/subscriptions/tenan-id/resourceGroups/rg-fabrikai102"

