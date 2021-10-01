from flask import Flask, jsonify, request

from apps import router as main_router
import methods


def make_app() -> Flask:

    app = Flask(__name__)

    main_router.install(app)

    return app
