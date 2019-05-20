class WebhookConf:
    API_TOKEN = '690204123:AAH2KDdj6S5If5TQkDvCANAIIJ-MBSfmkcE'
    WEBHOOK_HOST = 's156888.hostiman.com'
    WEBHOOK_PORT = 443
    WEBHOOK_LISTEN = '217.182.21.102'

    WEBHOOK_SSL_CERT = '/tel_pub/telegram_pub/project/ssl/server.crt'
    WEBHOOK_SSL_KEY = '/tel_pub/telegram_pub/project/ssl/server.key'

    WEBHOOK_URL_BASE = 'https://%s:%s' % (WEBHOOK_HOST, WEBHOOK_PORT)
    WEBHOOK_URL_PATH = '/%s/' % (API_TOKEN)

    PAYMENT_SECRET_WORD_ONE = 'vfct95uu'
    PAYMENT_SECRET_WORD_TWO = 'ktxso9lo'


class Configuration:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://telegram:telpass123@localhost/telegram'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'there are secret key'
    SECURITY_PASSWORD_SALT = 'some salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'
