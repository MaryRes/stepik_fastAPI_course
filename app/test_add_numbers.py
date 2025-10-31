import requests

response = requests.post(
    "http://127.0.0.1:8000/add_numbers", json={"number_1": 5, "number_2": 10}
)

print(response.json())  # {'result': 15}
