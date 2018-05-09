import json

from flask import Flask, make_response

from libs.comm_func import is_isbn_or_key
from libs.yunshu_book import YunShuBook

app = Flask(__name__)
app.config.from_object('config')


if __name__ == '__main__':
    app.run(debug=app.config["DEBUG"], host='0.0.0.0', port=8888)

