from apps import views


def install(app):
    app.add_url_rule(
        '/',
        view_func=views.BotView.as_view('home-page')
    )
