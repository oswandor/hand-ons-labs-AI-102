# Inicio Rápido: Azure AI Search con REST API

Este laboratorio le guiará a través del uso de la API REST de Azure AI Search para crear, cargar y consultar un índice de búsqueda.

## Requisitos previos

- Una suscripción de Azure
- Un servicio de Azure AI Search (puede utilizar el nivel gratuito F0)
- Visual Studio Code con la extensión "REST Client"

## Configuración inicial

1. Inicie Visual Studio Code.
2. Instale la extensión "REST Client" si aún no está instalada:
   - Haga clic en el icono de extensiones en la barra lateral
   - Busque "REST Client" y haga clic en "Instalar"

## Obtención de los datos de autenticación

### Encontrar el punto de conexión del servicio

1. Inicie sesión en [Azure Portal](https://portal.azure.com)
2. Encuentre su servicio de búsqueda
3. En la página de información general, copie la URL del servicio (por ejemplo, `https://miservicio.search.windows.net`)

### Obtener la clave de API (Opción 1)

1. En su servicio de búsqueda, vaya a "Configuración > Claves"
2. Copie una de las claves de administrador

### Configurar acceso basado en roles (Opción 2)

Si prefiere usar roles en lugar de claves:

1. Ejecute este comando en Azure CLI para obtener su token:
   ```
   az account get-access-token --scope https://search.azure.com/.default
   ```
2. Copie el token generado

## Usando el archivo de solicitudes REST

Abra el archivo `azure-search-rest.http` incluido en este laboratorio. Necesitará:

1. Reemplazar `PUT-YOUR-SEARCH-SERVICE-ENDPOINT-HERE` con el punto de conexión de su servicio
2. Reemplazar `PUT-YOUR-SEARCH-SERVICE-API-KEY-HERE` con su clave de API o token

## Ejecución de solicitudes REST

Una vez configurado, puede ejecutar las solicitudes en orden:

1. **Listar índices existentes**: Verifica la conexión y muestra cualquier índice actual
2. **Crear un nuevo índice**: Crea un esquema para datos de hoteles
3. **Cargar documentos**: Añade datos de ejemplo al índice
4. **Ejecutar una consulta**: Busca hoteles con vista al lago
5. **Obtener estadísticas**: Muestra el recuento de documentos y tamaño del índice
6. **Eliminar índice**: Limpia los recursos (opcional)

Para ejecutar una solicitud, haga clic en el enlace "Send Request" que aparece encima de cada definición de solicitud.

## Entendiendo el esquema del índice

El esquema define la estructura de los documentos en el índice:

- Campos con tipos de datos (String, Boolean, etc.)
- Atributos que determinan cómo se puede usar cada campo:
  - `searchable`: Permite búsqueda de texto completo
  - `filterable`: Permite filtrar resultados
  - `sortable`: Permite ordenar resultados
  - `facetable`: Permite agrupación para navegación por facetas

## Explorando más allá

- Intente diferentes consultas modificando el término de búsqueda
- Pruebe filtros agregando parámetros como `"filter": "Rating gt 4"`
- Explore la [documentación oficial](https://learn.microsoft.com/azure/search/search-get-started-rest) para más ejemplos

## Limpieza de recursos

Para evitar cargos innecesarios, elimine el índice cuando termine de experimentar usando la solicitud DELETE incluida en el archivo.
