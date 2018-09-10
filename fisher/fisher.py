from app import create_app

app = create_app()

if __name__ == '__main__':
    # threaded 开启多线程
    app.run(debug=app.config["DEBUG"], host='0.0.0.0', port=8888, threaded=True)
