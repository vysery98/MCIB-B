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

    '''
    # Ejemplo de headers
    headers = {
         'Content-Type': 'application/json',
         'Authorization': 'Bearer token'
    }
    '''
    
    # Datos que enviaremos en el cuerpo de la petición
    data = {
        'a': 5,
        'b': 3
    }
    
    # Solicitud POST enviando los datos en formato JSON
    response = requests.post(url, json = data, headers = headers) # Se agrega para aceptar HEADERS: headers = headers
    '''
    EJEMPLO CURL:
        curl -X POST http://localhost:8080/api/sumar -H "Content-Type: application/json" -d "{\"a\":5, \"b\":32}"

        EXPLICACIÓN PASO A PASO:
            - -X POST
                → Indica que el método HTTP es POST (por defecto sería GET).
            - http://localhost:8080/api/sumar
                → URL completa del endpoint al que se envía la solicitud.
                "/api/sumar" = ruta definida en Flask.
            - -H "Content-Type: application/json"
                → Header HTTP que especifica que el cuerpo de la petición está en formato JSON.
            - -d "{\"a\":5, \"b\":32}"
                → Datos enviados en el cuerpo de la petición.
                Aquí se envía un JSON con dos claves: a=5 y b=32.
                Las barras invertidas (\") son para escapar las comillas dentro del comando.
    
        RESULTADO ESPERADO:
            El servidor Flask recibe la petición POST en /api/sumar, procesa los datos y devuelve un JSON
            con el resultado de la suma
    '''
    
    print(response) # Devuelve Status 

    # Retornamos la respuesta en formato JSON
    return response.json()

# Ejecutamos la función y mostramos el resultado
print(request_sumar())
