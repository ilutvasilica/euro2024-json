import requests
import json
        
URL = 'https://techy-api.vercel.app/api/text'  

response = requests.get(URL)

print(response.status_code)
print(response.content)#aici intoarce byte

data = response.text#aici arata string
print(type(data))
print(data)

#aici vreau sa vad cate randuri sunt cu scopul de a le citi ,
#de aia le am pus cu read 
#am facut try si except ca sa nu dea eroare ca el nu poate sa faca
#read daca fisierul nu exista
try: 
   with open('mesaj.txt','r') as file:
    contor = len(file.readlines()) +1#aici citim randurile si adaugam 1 
except:
    contor = 1    #ca sa incepe de la 1 
    
# am pus 'a' cu scopul de a le aduga     
with open ('mesaj.txt','a') as file:
    file.write(f'{contor}{data}\n')   
    
    
    
    
