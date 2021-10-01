import requests
import json

from config import config


def send_message(chat_id, text):
    method = "sendMessage"
    url = config.webhook_url(method)
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
