import requests
import yaml
import random


def send_message(message):
    data = {"message": message}
    with open(r'security.yml') as file:
        documents = yaml.full_load(file)
        for keys, values in documents.items():
            if keys == 'users':
                i = random.randrange(0, len(values))
                requests.post(values[i]['tg'], data=data)
