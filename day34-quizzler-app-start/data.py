import requests

API_URL = "https://opentdb.com/api.php"
API_PARAMS = {
    "amount": 10,
    "category": 21,
    "type": "boolean"
}

responses = requests.get(API_URL, params=API_PARAMS)
responses.raise_for_status()
question_data = responses.json()["results"]
