import json
import uuid
import eventlet
from . import emit
from . import session
from . import socket_io
from .embedded.mfrc_service import ServiceMFRC

messages = {}
users = []
current_user = {}


@socket_io.on('connect')
def make_connection():
    session['uuid'] = uuid.uuid1()
    session['username'] = 'user-' + str(session['uuid'])
    current_user = {
        'sid': session['uuid'],
        'username': session['username']
    }
    users.append(current_user)
    message = 'User %s connected' % session['username']
    print(message)


@socket_io.on('sid request')
def get_session_id():
    send_message(message=str(session['uuid']), event='sid response')


def send_message(message, event, room=None):
    # last_id = max(messages.keys()) if len(messages) > 0 else 0
    # messages[last_id + 1] = {
    #     'message': message
    # }
    # print('Sending message-text: %s' % messages[last_id + 1])
    print('Sending message-text: %s' % message)
    if room is not None:
        unique_event = json.dumps({
            'event': event,
            'room': room
        })
        emit(unique_event, message)
    else:
        emit(event, message)


@socket_io.on('init_reader')
def init_reader(room):
    reader = ServiceMFRC()
    print('Reader activated')

    def get_data():
        return reader.do_read()

    # data = reader.do_read()
    data = eventlet.spawn(get_data())
    print('message from service manager: %s' % data['message'])
    reader_output(data=data, room=room)


def reader_output(data, room=None):
    message = {
        'message': data['message'],
        'data': data['data']
    }
    # last_id = max(messages.keys()) if len(messages) > 0 else 0
    # messages[last_id + 1] = {
    #     'message': message
    # }
    event = 'reader done'
    # event = 'reader done %s' % session['uuid']
    send_message(message=message, event=event, room=room)
