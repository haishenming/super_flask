from flask import request, jsonify

from app.libs.comm_func import is_isbn_or_key
from app.spider.yunshu_book import YunShuBook

from app.forms.book import SearchForm
from app.view_models.book import BookViewModel
from . import web


@web.route("/book/search")
def search():
    """
        q：关键字或isbn
        page：页码
    """
    # 判断用户上传来的是isbn还是关键字

    form = SearchForm(request.args)

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == "isbn":
            result = YunShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = YunShuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)

        return jsonify(result)

    else:
        return jsonify(form.errors)
