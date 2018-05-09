import json

from libs.comm_func import is_isbn_or_key
from libs.yunshu_book import YunShuBook

from fisher import app


@app.route("/book/search/<q>/<page>")
def search(q, page):
    """
        q：关键字或isbn
        page：页码
    """
    # 判断用户上传来的是isbn还是关键字
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == "isbn":
        result = YunShuBook.search_by_isbn(q)
    else:
        result = YunShuBook.search_by_keyword(q)

    return json.dumps(result), 200, {'content-type':'application/json'}