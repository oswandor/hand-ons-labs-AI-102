# Azure AI Document Intelligence - Formularios Personalizados
# ----------------------------------------------------------

Este quickstart muestra cómo utilizar Azure Document Intelligence para procesar y extraer datos de formularios con modelos personalizados y preintegrados.

## Requisitos previos

- Suscripción a Azure - Crea una gratis en https://azure.microsoft.com/free/
- Python 3.7 o superior
- Recurso de Document Intelligence en el portal de Azure
- Biblioteca de cliente de Document Intelligence:
  `pip install azure-ai-documentintelligence==1.0.0b4`

## Configuración

1. Crea un recurso de Document Intelligence en el portal de Azure
2. Obtén tu endpoint y clave del recurso
3. Actualiza las variables `endpoint` y `key` en el archivo `form_reader_quickstart.py`

## Funcionalidades incluidas en este ejemplo

1. **Entrenamiento de un modelo personalizado**
   - Código preparado para entrenar un modelo con tus propios formularios
   - Análisis de la estructura del modelo entrenado

2. **Análisis con modelo personalizado**
   - Extracción de datos usando un modelo previamente entrenado
   - Visualización de resultados con confianzas

3. **Análisis con modelo preintegrado**
   - Uso del modelo general "prebuilt-document"
   - Extracción de pares clave-valor y tablas
   - Visualización de resultados estructurados

## Ejecución del ejemplo

1. Asegúrate de tener instaladas las bibliotecas necesarias:
   ```
   pip install azure-ai-documentintelligence==1.0.0b4
   ```

2. Actualiza el endpoint y la clave en el script

3. Para usar el modelo preintegrado:
   ```
   python form_reader_quickstart.py
   ```
   
4. Para entrenar y usar un modelo personalizado:
   - Prepara tus datos de entrenamiento (archivos de formulario)
   - Sube los datos a un contenedor de Azure Blob Storage
   - Actualiza la URL de entrenamiento en el código
   - Descomenta la llamada a `analyze_custom_forms()` en la sección main

## Más información

- [Documentación de Document Intelligence](https://learn.microsoft.com/azure/ai-services/document-intelligence/)
- [Entrenamiento de modelos personalizados](https://learn.microsoft.com/azure/ai-services/document-intelligence/concept-custom)
