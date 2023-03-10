import requests
token = '9754150c5988bebaaf3f48c5064cb195'
response = requests.post('https://pokemonbattle.me:9104/pokemons', 
headers = {'Content-Type': 'application/json', 'trainer_token':token},
json = {"name": "Бабур",
"photo": "https://dolnikov.ru/pokemons/albums/011.png"})

print(response.text)


response_edit_name = requests.put('https://pokemonbattle.me:9104/pokemons', 
headers = {'Content-Type': 'application/json', 'trainer_token':token},
json = {"pokemon_id": 6059, "name": "Ричи",
"photo": ""})

print(response_edit_name.text)


response_catch = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', 
headers = {'Content-Type': 'application/json', 'trainer_token':token},
json = {"pokemon_id": 6059})

print(response_catch.text)


