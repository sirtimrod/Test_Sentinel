# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class DevConfig:

    TOKEN = os.getenv('TOKEN')
    WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
    NGROK = os.getenv('NGROK')

    def webhook_url(self, method):
        return f'https://{self.WEBHOOK_HOST}/bot{self.TOKEN}/' \
               f'{method}'


config = DevConfig()
