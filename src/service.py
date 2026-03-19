from src.repository import obtener_datos_crudos_clima

def procesar_clima(ciudad):
    try:
        datos_crudos = obtener_datos_crudos_clima(ciudad)
        
        clima_procesado = {
            "ciudad": datos_crudos["name"],
            "temperatura": datos_crudos["main"]["temp"],
            "Sensacion Termica": datos_crudos["main"]["feels_like"],
            "humedad": datos_crudos["main"]["humidity"],
            "presion_hpa": datos_crudos["main"]["pressure"],    
            "viento_vel": datos_crudos["wind"]["speed"],        
            "nubosidad": datos_crudos["clouds"]["all"],         
            "descripcion": datos_crudos["weather"][0]["description"]
        }
        return clima_procesado
        
    except Exception as e:
        return {"error": str(e)}