import requests

# Para hacer una solicitud a un API neceistamos la URL del endpoint y necesitamos headers

def request_info():
    url = 'http://localhost:8080/api/info'
    response = requests.get(url)

    return response.json()

# data = request_info()

# print(data)

# print(data.get('version'))

def request_sumar():
    url = 'http://localhost:8080/api/sumar'

#    header = {
#        'Content-Type': 'application/json',
#        'Authorization': 'Bearer token'
#    }

    data = {
        'a': "5",
        'b': 3
    }

    # response  = requests.post(url, json = data, headers = headers)
    response = request.post(url, json = data)
    print(response)
    return response.json()

print(request_sumar())