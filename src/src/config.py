import os

DATA_DIR_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'data')

DATABASE_URI = os.path.join(DATA_DIR_PATH, 'rfid-db.sqlite')
UPLOAD_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/images')

DATA_EXCEL_PATH = os.path.join(DATA_DIR_PATH, 'seed_data')

SECRET_KEY = 'the_secret_key'
