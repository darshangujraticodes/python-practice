'''
Python API handling 

'''


import requests
import json

api_url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(api_url)

# final api value is fetched and 
api_data = response.json()

json_str = json.dumps(api_data, indent = 4)

print('\napi data type = ',type(api_data))

print('\njson conversion = ',json_str, type(json_str))









