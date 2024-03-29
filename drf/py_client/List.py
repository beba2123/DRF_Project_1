import requests
from getpass import getpass
auth_endpoint = "http://127.0.0.1:8000/api/auth/"

# first create a session to the server and receive an authentication token
password = getpass()
auth_response = requests.post(auth_endpoint, json={'username': 'beba', 'password':password})
print(auth_response.json())

if  auth_response.status_code == 200:
     token = auth_response.json().get('token')
     header = {
          'Authorization': f'Token {token}'
     }
     endpoint = "http://127.0.0.1:8000/api/products/"


     get_response = requests.get(endpoint, headers=header)
     print(get_response.json())
