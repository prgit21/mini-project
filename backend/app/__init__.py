from flask import Flask, make_response


def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(error):
        return make_response("404", 404)

    @app.errorhandler(500)
    def internal_error(exception):
        return "Some internal error has taken place. Alert somebody!"

    @app.route('/')
    def hello():
        return "hello"
    return app
