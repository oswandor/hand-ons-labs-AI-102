import os
import requests
import json
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración del servicio de búsqueda
search_endpoint = os.getenv("SEARCH_ENDPOINT")
search_api_key = os.getenv("SEARCH_API_KEY")
search_api_version = "2024-07-01"

# Nombre del índice
index_name = "hotels-quickstart-python"

# Encabezados para autenticación y tipo de contenido
headers = {
    'Content-Type': 'application/json',
    'api-key': search_api_key
}

def list_indexes():
    """Lista los índices existentes en el servicio de búsqueda"""
    url = f"{search_endpoint}/indexes?api-version={search_api_version}&$select=name"
    response = requests.get(url, headers=headers)
    
    print("\n=== Índices existentes ===")
    if response.status_code == 200:
        indexes = response.json()
        if indexes['value']:
            for index in indexes['value']:
                print(f"- {index['name']}")
        else:
            print("No se encontraron índices.")
    else:
        print(f"Error al listar índices: {response.status_code} - {response.text}")

def create_index():
    """Crea un nuevo índice de búsqueda"""
    # Definición del esquema del índice
    index_definition = {
        "name": index_name,
        "fields": [
            {"name": "HotelId", "type": "Edm.String", "key": True, "filterable": True},
            {"name": "HotelName", "type": "Edm.String", "searchable": True, "filterable": False, "sortable": True, "facetable": False},
            {"name": "Description", "type": "Edm.String", "searchable": True, "filterable": False, "sortable": False, "facetable": False, "analyzer": "es.lucene"},
            {"name": "Category", "type": "Edm.String", "searchable": True, "filterable": True, "sortable": True, "facetable": True},
            {"name": "Tags", "type": "Collection(Edm.String)", "searchable": True, "filterable": True, "sortable": False, "facetable": True},
            {"name": "ParkingIncluded", "type": "Edm.Boolean", "filterable": True, "sortable": True, "facetable": True},
            {"name": "LastRenovationDate", "type": "Edm.DateTimeOffset", "filterable": True, "sortable": True, "facetable": True},
            {"name": "Rating", "type": "Edm.Double", "filterable": True, "sortable": True, "facetable": True},
            {"name": "Address", "type": "Edm.ComplexType", 
                "fields": [
                {"name": "StreetAddress", "type": "Edm.String", "filterable": False, "sortable": False, "facetable": False, "searchable": True},
                {"name": "City", "type": "Edm.String", "searchable": True, "filterable": True, "sortable": True, "facetable": True},
                {"name": "StateProvince", "type": "Edm.String", "searchable": True, "filterable": True, "sortable": True, "facetable": True},
                {"name": "PostalCode", "type": "Edm.String", "searchable": True, "filterable": True, "sortable": True, "facetable": True},
                {"name": "Country", "type": "Edm.String", "searchable": True, "filterable": True, "sortable": True, "facetable": True}
                ]
            }
        ]
    }
    
    url = f"{search_endpoint}/indexes?api-version={search_api_version}"
    response = requests.post(url, headers=headers, json=index_definition)
    
    print("\n=== Creación de índice ===")
    if response.status_code in [201, 200]:
        print(f"Índice '{index_name}' creado exitosamente.")
    else:
        print(f"Error al crear índice: {response.status_code} - {response.text}")

def upload_documents():
    """Carga documentos al índice"""
    documents = {
        "value": [
            {
                "@search.action": "upload",
                "HotelId": "1",
                "HotelName": "Hotel Continental Madrid",
                "Description": "El hotel está idealmente ubicado en la arteria comercial principal de la ciudad en el corazón de Madrid. A pocos minutos se encuentra la Puerta del Sol y el centro histórico de la ciudad, así como otros lugares de interés que hacen de Madrid una de las ciudades más atractivas y cosmopolitas de España.",
                "Category": "Boutique",
                "Tags": ["piscina", "aire acondicionado", "conserje"],
                "ParkingIncluded": False,
                "LastRenovationDate": "1970-01-18T00:00:00Z",
                "Rating": 3.6,
                "Address": {
                    "StreetAddress": "Gran Vía 677",
                    "City": "Madrid",
                    "StateProvince": "Madrid",
                    "PostalCode": "28013",
                    "Country": "España"
                }
            },
            {
                "@search.action": "upload",
                "HotelId": "2",
                "HotelName": "Hotel Antiguo Siglo",
                "Description": "El hotel está situado en una plaza del siglo XIX, que ha sido ampliada y renovada según los más altos estándares arquitectónicos para crear un hotel moderno, funcional y de primera clase en el que el arte y los elementos históricos únicos coexisten con las comodidades más modernas.",
                "Category": "Boutique",
                "Tags": ["piscina", "wifi gratis", "conserje"],
                "ParkingIncluded": False,
                "LastRenovationDate": "1979-02-18T00:00:00Z",
                "Rating": 3.6,
                "Address": {
                    "StreetAddress": "Calle Alcalá 140",
                    "City": "Barcelona",
                    "StateProvince": "Cataluña",
                    "PostalCode": "08009",
                    "Country": "España"
                }
            },
            {
                "@search.action": "upload",
                "HotelId": "3",
                "HotelName": "Hotel Panorama Gastronómico",
                "Description": "El Hotel destaca por su excelencia gastronómica bajo la dirección de William Dough, quien asesora y supervisa todos los servicios de restaurante del Hotel. Desde sus ventanas se puede disfrutar de una vista espectacular al lago.",
                "Category": "Resort y Spa",
                "Tags": ["aire acondicionado", "bar", "desayuno continental", "vista al lago"],
                "ParkingIncluded": True,
                "LastRenovationDate": "2015-09-20T00:00:00Z",
                "Rating": 4.8,
                "Address": {
                    "StreetAddress": "Avenida Diagonal 393",
                    "City": "Sevilla",
                    "StateProvince": "Andalucía",
                    "PostalCode": "41001",
                    "Country": "España"
                }
            },
            {
                "@search.action": "upload",
                "HotelId": "4",
                "HotelName": "Hotel Palacio Sublime",
                "Description": "El Hotel Palacio Sublime está ubicado en el corazón del centro histórico de Sublime en un área extremadamente vibrante y animada a poca distancia a pie de los sitios y puntos de referencia de la ciudad y está rodeado por la extraordinaria belleza de iglesias, edificios, tiendas y monumentos. El Palacio Sublime forma parte de un palacio restaurado con amor de 1800.",
                "Category": "Boutique",
                "Tags": ["conserje", "vista", "servicio de recepción 24 horas"],
                "ParkingIncluded": True,
                "LastRenovationDate": "1960-02-06T00:00:00Z",
                "Rating": 4.6,
                "Address": {
                    "StreetAddress": "Calle San Pedro 74",
                    "City": "Valencia",
                    "StateProvince": "Comunidad Valenciana",
                    "PostalCode": "46002",
                    "Country": "España"
                }
            }
        ]
    }
    
    url = f"{search_endpoint}/indexes/{index_name}/docs/index?api-version={search_api_version}"
    response = requests.post(url, headers=headers, json=documents)
    
    print("\n=== Carga de documentos ===")
    if response.status_code == 200:
        print("Documentos cargados exitosamente.")
    else:
        print(f"Error al cargar documentos: {response.status_code} - {response.text}")

def search_documents(search_term="lago vista"):
    """Busca documentos en el índice"""
    search_payload = {
        "search": search_term,
        "select": "HotelId, HotelName, Tags, Description",
        "searchFields": "Description, Tags",
        "count": True
    }
    
    url = f"{search_endpoint}/indexes/{index_name}/docs/search?api-version={search_api_version}"
    response = requests.post(url, headers=headers, json=search_payload)
    
    print(f"\n=== Búsqueda de '{search_term}' ===")
    if response.status_code == 200:
        results = response.json()
        print(f"Resultados encontrados: {results.get('@odata.count', 0)}")
        
        for result in results.get('value', []):
            print(f"\nHotel: {result['HotelName']}")
            print(f"ID: {result['HotelId']}")
            print(f"Puntuación: {result.get('@search.score')}")
            print(f"Descripción: {result['Description']}")
            print(f"Tags: {', '.join(result['Tags'])}")
    else:
        print(f"Error al buscar documentos: {response.status_code} - {response.text}")

def get_index_stats():
    """Obtiene estadísticas del índice"""
    url = f"{search_endpoint}/indexes/{index_name}/stats?api-version={search_api_version}"
    response = requests.get(url, headers=headers)
    
    print("\n=== Estadísticas del índice ===")
    if response.status_code == 200:
        stats = response.json()
        print(f"Cantidad de documentos: {stats['documentCount']}")
        print(f"Tamaño de almacenamiento: {stats['storageSize']} bytes")
        print(f"Tamaño del índice de vectores: {stats['vectorIndexSize']} bytes")
    else:
        print(f"Error al obtener estadísticas: {response.status_code} - {response.text}")

def delete_index():
    """Elimina el índice"""
    url = f"{search_endpoint}/indexes/{index_name}?api-version={search_api_version}"
    response = requests.delete(url, headers=headers)
    
    print("\n=== Eliminación del índice ===")
    if response.status_code == 204:
        print(f"Índice '{index_name}' eliminado exitosamente.")
    else:
        print(f"Error al eliminar índice: {response.status_code} - {response.text}")

def main():
    print("=== Azure AI Search Demo en Python ===")
    
    # Verificar la configuración
    if search_endpoint == "https://your-search-service.search.windows.net" or search_api_key == "your-search-admin-key":
        print("ERROR: Actualice las variables search_endpoint y search_api_key con los valores de su servicio Azure AI Search")
        return
    
    # Ejecutar operaciones de búsqueda
    list_indexes()
    create_index()
    upload_documents()
    search_documents()
    get_index_stats()
    
    # Descomente la siguiente línea para eliminar el índice al final
    # delete_index()

if __name__ == "__main__":
    main()
