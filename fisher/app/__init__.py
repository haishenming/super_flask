from flask import Flask


def create_app():
    """ 创建Flask app对象 """

    app = Flask(__name__)
    app.config.from_object('config')
