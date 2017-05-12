import datetime
from ..config import SECRET_KEY as key
from werkzeug.security import generate_password_hash, check_password_hash


class AuthManager():
    @staticmethod
    def secure_password(raw_password):
        """
        Hashes the password using werkzeug.security.generate_password_hash function
        :param raw_password:
        :return: string
        """
        return generate_password_hash(raw_password)

    @staticmethod
    def check_password(password):
        """
        Validates the password hash using werkzeug.security.check_password_hash function
        :param password:
        :return: bool
        """
        return check_password(password)

    @staticmethod
    def encode_auth_token(user):
        """
        Encodes a new auth token for cookie
        :param user:
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': user.email
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'ERROR: Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'ERROR: Invalid token. Please log in again.'
