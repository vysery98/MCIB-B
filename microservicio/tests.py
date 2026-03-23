import requests  # Librería para hacer solicitudes HTTP en Python

# Función para consultar información del API
def request_info():
    # Definimos la URL del endpoint
    url = 'http://localhost:8080/api/info'
    
    # Hacemos una solicitud GET al endpoint
    response = requests.get(url)

    # Retornamos la respuesta en formato JSON
    return response.json()

# Función para enviar datos al endpoint de suma
def request_sumar():
    # Definimos la URL del endpoint
    url = 'http://localhost:8080/api/sumar'

    # Ejemplo de headers (comentados porque no son necesarios en este caso)
    ''' headers = {
         'Content-Type': 'application/json',
         'Authorization': 'Bearer token'
     }'''

    # Datos que enviaremos en el cuerpo de la petición
    data = {
        'a': 5,   # Debe ser entero, no string (corregido)
        'b': 3
    }

    # Solicitud POST enviando los datos en formato JSON
    response = requests.post(url, json=data)

    print(response) # Devuelve Status 

    # Retornamos la respuesta en formato JSON
    return response.json()

# Ejecutamos la función y mostramos el resultado
print(request_sumar())
