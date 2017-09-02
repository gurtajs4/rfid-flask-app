from src import app

if __name__ == '__main__':
    if not app.debug:
        app.run(host='0.0.0.0', port=80, debug=False)
    else:
        app.run(host='127.0.0.1', port=5200, debug=True)
