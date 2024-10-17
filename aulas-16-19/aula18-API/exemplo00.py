#Biblioteca Requests

import requests
from pydantic import BaseModel

#Pydantic - Valida e deserializa o código

class PokemonSchema(BaseModel): #Contrato de dados, schema de dados, a view
    
    name:str
    type:str
    
    class Config:
        from_attributes = True
        
def capturar_pokemon(id: int) -> PokemonSchema:

    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}') #select
   
    #exemplo
    """response = requests.get(url='https://www.mercadolivre.com.br/')
    print(response.text)"""

    """URL = ('https://pokeapi.co/api/v2/pokemon/25')
    response = requests.get(URL)"""
    
    data = response.json()
    data_types = data['types']
    types_list = [] #Cria um lista vazia
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ','.join(types_list) #Transforma um lista em uma string com virgulas

    return PokemonSchema(name=data['name'], type=types)

if __name__ == "__main__":
    
    print(capturar_pokemon(25))
    print(capturar_pokemon(6))
    print(capturar_pokemon(3))



"""requests.post #create

requests.put #update

requests.delete #delete
"""
