"""Main app/routing file for Twitoff"""

from flask import Flask, render_template
import json
from data_model import DB, User, Tweet


def create_app():
    """Creating and configuring an instance of the Flask application"""
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def landing():
        DB.create_all()
        nick = User(id=1,name="nick")
        elon = User(id=2,name="elonmusk")
        app_user = User(id=3,name='app_user')
        DB.session.add(app_user)
        DB.session.add(elon)
        DB.session.add(nick)
        DB.session.commit()
        args = {'title': "Landing", 'body': "landing body"}
        return render_template("base.html", **args)

    @app.route('/products')
    def products():
        new_tweet(id=1, text='tweet', user_id=1)
        DB.session.add(new_tweet)
        DB.session.commit()
        return render_template("base.html", title="Products", body="products in the body")

    return app

if __name__ == "__main__":
    create_app().run(host='0.0.0.0', port=8888)
