import requests

PARAMETERS = {
            "amount" : 20,
            "type" : "boolean",
}

trivia_request = requests.get(url="https://opentdb.com/api.php", params=PARAMETERS)
trivia_request.raise_for_status()
question_data = trivia_request.json()["results"]