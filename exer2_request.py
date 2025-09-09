import requests
import json

URL = 'https://techy-api.vercel.app/api/json'   

response= requests.get(URL) 

print(response.status_code)
print(response.content)

print(response.json(),type(response.json()))

json_response = response.json()
print(json_response['message'])# aici pt ca ii dictionar folosim mesage

try:
   with open ('techy.json','r') as file:
   
    dictionarul_citit= json.load(file)
except:
      dictionarul_citit = {'mesaje':[]}  

dictionarul_citit['mesaje'].append(json_response['message'])

with open ('techy.json','a') as file:
    json.dump(dictionarul_citit,file)
    