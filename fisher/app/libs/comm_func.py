# 公共函数

def is_isbn_or_key(q):
    """ 判断传入参数是isbn还是关键字 """
    isbn_or_key = "key"
    if len(q) == 13 and q.isdigit():
        # 是否为isbn
        isbn_or_key = "isbn"
    short_q = q.replace('-', '')
    if '-' in q and len(short_q) == 13 and short_q.isdigit():
        isbn_or_key = "isbn"

    return isbn_or_key