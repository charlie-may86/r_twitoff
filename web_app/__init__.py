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

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

# this is where the database lives
# DATABASE_URL = "sqlite:///twitoff_dspt7_development.db" # using relative filepath
DATABASE_URL = "sqlite:////Users/charliemay/Desktop/Lambda/DSPT7/r_twitoff/web_app/twitoff_mike.db"


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)