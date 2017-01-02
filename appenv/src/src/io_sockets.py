import uuid
from . import emit
from . import session
from . import socket_io

messages = {}
users = {}


# class IOSocketManager(object):


@socket_io.on('connect')
def make_connection():
    session['uuid'] = uuid.uuid1()
    session['username'] = 'user-' + str(session['uuid'])
    users[session['uuid']] = {
        'username': session['username']
    }
    print('User %s connected' % session['username'])


def send_message(message, event):
    last_id = max(messages.keys()) if len(messages) > 0 else 0
    messages[last_id + 1] = {
        'message': message
    }
    print(messages[last_id + 1])
    emit(event, message)


def reader_output(data):
    message = {
        'message': data['message'],
        'data': data['data']
    }
    last_id = max(messages.keys()) if len(messages) > 0 else 0
    messages[last_id + 1] = {
        'message': message
    }
    send_message(message=message, event='reader-done')
