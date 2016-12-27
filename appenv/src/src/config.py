import os

sqlite_dir_path = os.path.join(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), 'data')
DATABASE_URI = os.path.join(sqlite_dir_path, 'rfid-db.sqlite')

SECRET_KEY = 'the_secret_key'
