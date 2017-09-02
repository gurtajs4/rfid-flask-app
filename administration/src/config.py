import os

DATA_DIR_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'data')

UPLOAD_URI = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/images')

TEST_DATABASE_URI = os.path.join(DATA_DIR_PATH, 'test-db.sqlite')
DEV_DATABASE_URI = os.path.join(DATA_DIR_PATH, 'dev-db.sqlite')
PROD_DATABASE_URI = os.path.join(DATA_DIR_PATH, 'rfid-db.sqlite')
DATABASE_URI = PROD_DATABASE_URI if not os.environ['FLASK_DEBUG'] else DEV_DATABASE_URI

DATA_EXCEL_PATH = os.path.join(DATA_DIR_PATH, 'seed_data')

SECRET_KEY = os.environ['SECRET_KEY'] if os.environ.has_key('SECRET_KEY') else 'the_secret_key'
