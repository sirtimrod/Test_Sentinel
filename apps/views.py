from flask import request, jsonify
from flask.views import MethodView

import methods


class BotView(MethodView):

    def get(self):
        return '<h1>Hello, friend !!</h1>'

    def post(self):

        message = request.json['message']
        methods.send_message(message)

        return jsonify({'Status': 'OK'}), 200
