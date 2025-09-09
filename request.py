

import requests
import json

zip_code = 90210
country ='US'

country = 'us'
zip_code = '79015'

zip_code = '10045'
country = 'us'

URL = f"https://api.zippopotam.us/{country}/{zip_code}"

response = requests.get(URL)

print(response.status_code)
print(response.content)

json_response= json.loads(response.content)
print(type(json_response),json_response)
print(json_response)

print('Orasul este',json_response ['places'][0]['place name']) 

# atentie [0] vine de la dictzionar,ca inainte de place ii dictionarul mare unde exista place name ,si
#apoi scrii New York.

# with open('city_text','a',encoding='utf-8') as fwriter:
       # fwriter.write(json_response)
        #fwriter.write('\n')

