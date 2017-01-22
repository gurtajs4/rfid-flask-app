import os

sqlite_dir_path = os.path.join(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'data')
DATABASE_URI = os.path.join(sqlite_dir_path, 'rfid-db.sqlite')
UPLOAD_URI = os.path.join(os.path.abspath(__file__), 'static/images')

SECRET_KEY = 'the_secret_key'
