import requests

# Para hacer una solicitud a un API neceistamos la URL del endpoint y necesitamos headers

def request_info():
    url = 'http://localhost:8080/api/info'
    response = requests.get(url)

    return response.json()

data = request_info()

print(data)

print(data.get('version'))