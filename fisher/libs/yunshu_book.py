# 书籍

from .httper import HTTP

from flask import current_app


class YunShuBook:
    per_page = 15  # 每页数量

    isbn_url = "http://t.yushu.im/v2/book/isbn/{}"
    keyword_url = "http://t.yushu.im/v2/book/search?q={}&count={}&start={}"

    def __init__(self, url):
        self.url = url

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)

        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config["PER_PAGE"],
                                     cls.calculate_start(page))
        result = HTTP.get(url)

        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config["PER_PAGE"]