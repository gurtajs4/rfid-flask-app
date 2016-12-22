from .mappers import ApiJSONEncoder
from .. import app
from ..core import api_manager


class SqliteApiManager:
    def __init__(self):
        for model_name in app.config['API_MODELS']:
            model_class = app.config['API_MODELS'][model_name]
            api_manager.create_api(model_class, methods=['GET', 'POST'])
        self.api_session = api_manager.session
        self.crud_url_models = app.config['CRUD_URL_MODELS']

    def get_models(self, model_name):
        model_class = self.crud_url_models[model_name]
        data = [ApiJSONEncoder.key_json_encode(model_instance) for model_instance in model_class]
        return data

    def get_single(self, model_name, id):
        model_class = self.crud_url_models[model_name]
        model_instance = self.api_session.query(model_class).filter(model_class.id == id).first()
        data = ApiJSONEncoder.key_json_encode(model_instance)
        return data
