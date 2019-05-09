from app import app, bot
from config import WebhookConf
import bot_views
import time


if __name__ == '__main__':
    bot.remove_webhook()
    time.sleep(2)
    bot.set_webhook(url=WebhookConf.WEBHOOK_URL_BASE + WebhookConf.WEBHOOK_URL_PATH,
                    certificate=open(WebhookConf.WEBHOOK_SSL_CERT, 'r'))
    app.run()
