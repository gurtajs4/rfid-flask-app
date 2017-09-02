from .. import app
from ..services.service_manager import ServiceManager
from ..services.storage_manager import StorageManager
from ..services.serializers import JSONSerializer as jserial
from flask import jsonify, request, Response, send_file

service_manager = ServiceManager()

import core_views
import user_views
import key_views
import session_views
import user_session_views