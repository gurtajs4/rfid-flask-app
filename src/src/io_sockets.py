import json
import uuid
from . import emit
from . import session
from . import socket_io
from .embedded.mfrc_service import ServiceMFRC
from .services.service_manager import ServiceManager

messages = {}
users = []
current_user = {}


@socket_io.on('connect')
def make_connection():
    session['uuid'] = uuid.uuid4()
    session['username'] = 'user-' + str(session['uuid'])
    current_user = {
        'sid': session['uuid'],
        'username': session['username'],
        'room': session.get('room')
    }
    users.append(current_user)
    message = 'User %s connected' % session['username']
    print(message)


@socket_io.on('client sid request')
def get_client_session_id():
    send_message(message=str(session['uuid']), event='sid response')


def send_message(message, event, room=None):
    print('Sending message-text: %s' % message)
    if room is not None:
        # unique_event = event + ' ' + room
        emit(event, message, room=room)
    else:
        emit(event, message)


@socket_io.on('init reader')
def init_reader(room):
    reader = ServiceMFRC()
    print('Reader activated')
    data = reader.do_read()
    print('message from service manager: %s' % data['message'])
    reader_output(data=data, room=room)


def reader_output(data, room=None):
    message = {
        'message': data['message'],
        'data': data['data']
    }
    event = 'reader done'
    send_message(message=message, event=event, room=room)


@socket_io.on('download template')
def download_template():
    print('From server - socket event - download template')
    file = ServiceManager.get_excel_template()
    room = session.get('room')
    message = {'file': file}
    print('From server - socket response - room is %s' % room)
    send_message(message=message, event='download begins', room=room)
