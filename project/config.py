class WebhookConf:
    API_TOKEN = '690204123:AAH2KDdj6S5If5TQkDvCANAIIJ-MBSfmkcE'
    WEBHOOK_HOST = 's156888.hostiman.com'
    WEBHOOK_PORT = 443
    WEBHOOK_LISTEN = '0.0.0.0'

    WEBHOOK_SSL_CERT = '/keys/cert.pem'
    WEBHOOK_SSL_KEY = '/keys/key.pem'

    WEBHOOK_URL_BASE = 'https://%s:%s' % (WEBHOOK_HOST, WEBHOOK_PORT)
    WEBHOOK_URL_PATH = '/%s/' % (API_TOKEN)


class Configuration:
    DEBUG = True
    HOST = WebhookConf.WEBHOOK_LISTEN
    PORT = WebhookConf.WEBHOOK_PORT
    SSL_CONTEXT = (WebhookConf.WEBHOOK_SSL_CERT, WebhookConf.WEBHOOK_SSL_KEY)