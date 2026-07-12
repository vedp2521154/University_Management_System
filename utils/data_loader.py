import json


def load_data():
    with open("data/university_data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data