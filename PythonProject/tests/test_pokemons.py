import requests
import pytest

# Базовый URL
host = 'https://api.pokemonbattle.me:9104'

# Токен тренера
token = "b07dfdc08a60bdc58d8b2557a3c3aba5"

# Проверка статуса кода
def test_status_code():
    response = requests.get(f'{host}/trainers', params={'trainer_id': 2357})
    assert response.status_code == 200

# Проверка части тела ответа
def test_part_of_body():
    response = requests.put(f'{host}/trainers', headers={"trainer_token": token}, json={
        "name": "Канзас",
        "city": "Tokyo"
    })
    assert response.json()["message"] == "Информация о тренере обновлена"

# Параметризованный тест для проверки JSON-ответа
@pytest.mark.parametrize('key, value', [
    ("trainer_name", "Канзас"),
    ("id", "2357"),
    ("city", "Tokyo")
])
def test_response_json(key, value):
    response = requests.get(f'{host}/trainers', params={'trainer_id': 2357})
    assert response.json()[key] == value
