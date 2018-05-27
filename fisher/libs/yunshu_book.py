# 书籍

from .httper import HTTP


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
        url = cls.keyword_url.format(keyword, cls.per_page, (page - 1) * cls.per_page)
        result = HTTP.get(url)

        return result
