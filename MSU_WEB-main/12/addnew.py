import json

data = {
    "id": "etalon",
    "password": "default",
    "img": "default",
    "name": "default",
    "description": "default",
    "skills": [
        "default"
    ],

    "wish": [
        "default"
    ]
}

with open(data["id"] + ".txt", 'w', encoding='utf-8') as f:
    f.write(json.dumps(data))
