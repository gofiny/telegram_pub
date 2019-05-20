import sys

activate_this = '/tel_pub/telegram_pub/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
sys.path.insert(0, '/tel_pub/telegram_pub/project/')

from app import app as application
