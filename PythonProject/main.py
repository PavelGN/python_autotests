import requests

# Ваш токен
token = "b07dfdc08a60bdc58d8b2557a3c3aba5"

# Регистрация тренера
response_register = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json={
    "trainer_token": token,
    "email": "gerrar111@dolnikov.ru",
    "password": "Iloveqa1"
}, headers={"Content-Type": "application/json"})

print("Регистрация тренера:", response_register.text)

# Подтверждение электронной почты
response_activation = requests.post('https://api.pokemonbattle.me:9104/trainers/confirm_email', json={
    "trainer_token": token
}, headers={"Content-Type": "application/json"})

print("Статус подтверждения электронной почты:", response_activation.status_code)

if response_activation.status_code == 200:
    print('Подтверждение прошло успешно')
else:
    print('Подтверждение не удалось')

# Создание покемона
response_create_pokemon = requests.post('https://api.pokemonbattle.me:9104/pokemons', json={
    "name": "generate",
    "photo": "generate"
}, headers={"Content-Type": "application/json", "trainer_token": token})

print("Создание покемона:", response_create_pokemon.json())

# Обновление информации о покемоне
response_update_pokemon = requests.put('https://api.pokemonbattle.me:9104/pokemons', json={
    "pokemon_id": "11103",
    "name": "Tremor",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers={"Content-Type": "application/json", "trainer_token": token})

print("Обновление информации о покемоне:", response_update_pokemon.json())

# Добавление в покебол
response_add_pokeball = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json={
    "pokemon_id": "11103"
}, headers={"Content-Type": "application/json", "trainer_token": token})

print("Добавление в покебол:", response_add_pokeball.json())
