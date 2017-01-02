from src import app
from src import socket_io


if __name__ == '__main__':
    socket_io.run(host='0.0.0.0', port=80, debug=True)
    # app.run(host='0.0.0.0', port=80, debug=True)
