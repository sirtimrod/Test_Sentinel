import os

from flask import request, jsonify
from flask.views import MethodView

import requests
import methods


class BotView(MethodView):

    def get(self):

        if int(os.getenv('CHAT_ID')) == 0:
            return '<h1>There is no one yet :((</h1>'

        message = "Hello, my friend :)"
        methods.send_message(int(os.getenv('CHAT_ID')), message)

        return '<h1>Hello, friend !!</h1>'

    def post(self):

        r = request.get_json()
        methods.write_json(r)
        chat_id = r['message']['chat']['id']
        print(chat_id)
        os.environ['CHAT_ID'] = str(chat_id)

        return jsonify(r)


# https://api.telegram.org/bot1949388923:AAHVYYyR8CuE69NzK64tktCeHJYtjI1X01s/setWebhook?url=https://3612-77-234-205-2.ngrok.io