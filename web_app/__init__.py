# web_app/__init__.py
'''
this init file creates the app - it is the entry point into the 
web_app folder
'''
from flask import Flask

'''
By importing these routes, I am able to initialize each page
when running my web_app.
'''
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)