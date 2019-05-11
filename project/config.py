class WebhookConf:
    API_TOKEN = '690204123:AAH2KDdj6S5If5TQkDvCANAIIJ-MBSfmkcE'
    WEBHOOK_HOST = 's156888.hostiman.com'
    WEBHOOK_PORT = 443
    WEBHOOK_LISTEN = '217.182.21.102'

    WEBHOOK_SSL_CERT = '/keys/cert.pem'
    WEBHOOK_SSL_KEY = '/keys/priv.key'

    WEBHOOK_URL_BASE = 'https://%s:%s' % (WEBHOOK_HOST, WEBHOOK_PORT)
    WEBHOOK_URL_PATH = '/%s/' % (API_TOKEN)


class Configuration:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://telegram_pub:telpass123@localhost/telegram'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'there are secret key'
