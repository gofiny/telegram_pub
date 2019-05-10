class WebhookConf:
    API_TOKEN = '690204123:AAH2KDdj6S5If5TQkDvCANAIIJ-MBSfmkcE'
    WEBHOOK_HOST = 's156888.hostiman.com'
    WEBHOOK_PORT = 443
    WEBHOOK_LISTEN = '217.182.21.102'

    WEBHOOK_SSL_CERT = '/keys/fullchain.pem'
    WEBHOOK_SSL_KEY = '/keys/privkey.pem'

    WEBHOOK_URL_BASE = 'https://%s:%s' % (WEBHOOK_HOST, WEBHOOK_PORT)
    WEBHOOK_URL_PATH = '/%s/' % (API_TOKEN)


class Configuration:
    DEBUG = True
