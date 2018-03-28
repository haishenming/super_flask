from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "hello, Leo"

# 两种路由注册方式
app.add_url_rule('/hello', view_func=hello)


app.run(debug=True)

