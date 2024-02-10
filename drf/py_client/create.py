import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data={
    'title':  'pine_apple'
}

get_response = requests.post(endpoint, data)
print(get_response.json())