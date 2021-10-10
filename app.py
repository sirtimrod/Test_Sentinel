from flask import Flask

from apps import router as main_router


def make_app() -> Flask:

    app = Flask(__name__)

    main_router.install(app)

    return app
