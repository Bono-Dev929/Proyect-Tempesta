import requests
import json 
from src.config import API_KEY, BASE_URL

def obtener_datos_crudos_clima(ciudad):
    """Hace la petición GET a OpenWeatherMap."""
    parametros = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }
    
    respuesta = requests.get(BASE_URL, params=parametros)
    
    if respuesta.status_code == 200:
        datos_crudos = respuesta.json()
        
        with open("clima_crudo.json", "w", encoding="utf-8") as archivo:
            
            json.dump(datos_crudos, archivo, indent=4, ensure_ascii=False)
        
        
        return datos_crudos 
    elif respuesta.status_code == 404:
        
        raise Exception("No pudimos encontrar esa ciudad en el radar. Revisá la ortografía.")
    else:
        
        raise Exception(f"Error de conexión con el servidor meteorológico. (Código: {respuesta.status_code})")