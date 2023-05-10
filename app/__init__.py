from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)


    from .routes import hello_books_bp, books_bp

    app.register_blueprint(hello_books_bp)
    app.register_blueprint(books_bp)

    return app