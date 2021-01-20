class WebhookConf:
    API_TOKEN = ''
    WEBHOOK_HOST = ''
    WEBHOOK_PORT = 443
    WEBHOOK_LISTEN = ''

    WEBHOOK_SSL_CERT = ''
    WEBHOOK_SSL_KEY = ''

    WEBHOOK_URL_BASE = 'https://%s:%s' % (WEBHOOK_HOST, WEBHOOK_PORT)
    WEBHOOK_URL_PATH = '/%s/' % (API_TOKEN)

    PAYMENT_SECRET_WORD_ONE = ''
    PAYMENT_SECRET_WORD_TWO = ''


class Configuration:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://telegram:telpass123@localhost/telegram'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ''
    SECURITY_PASSWORD_SALT = ''
    SECURITY_PASSWORD_HASH = 'bcrypt'
