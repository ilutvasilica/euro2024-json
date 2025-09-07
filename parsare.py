
import json
from pprint import pprint

#link ='https://dontpad.com/euro2024'

#Versiunea 1 -citire din fisier + parsare
with open ('euro_2024.json')as file_handler:
    #citesc continutul 
    continut = file_handler.read()
    print((type(continut),continut))
    #parsez continutul
    continut_parsat = json.loads(continut)
    print(type(continut_parsat),continut_parsat)
  
  #sau acelasi lucru ,ce ii jos ii la fel cu ce ii sus   ,versiunea 2-parsaee la citire(direct)
with open ('euro_2024.json')as file_handler:
    continut_parsat = json.load(file_handler)    
    print(type(continut_parsat),continut_parsat)
    

print(continut_parsat.keys())   

tara_cautata = 'Romania'

groups = continut_parsat['groups']#am printat  daor valoarea 
pprint(type(groups))    
pprint(groups)
    
for gr in groups:
    print(type(gr))   
    pprint(gr['teams']) 
    for team in gr['teams']:
        print(type(team))
        pprint(team)
         
        if team['name']  == tara_cautata:
            print(f'{tara_cautata} se afla in grupa {gr['name']}')
            break