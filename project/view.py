from app import app
from flask import render_template
from flask import request
from models import Subscriptions
from bot_views import write_stuff


@app.route('/')
def index():
    return render_template('main/index.html')


@app.route('/new_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'GET':
        subs = Subscriptions.query.all()
        return render_template('main/create_post.html', subs=subs)

    if request.method == 'POST':
        title = request.form.get('title', None)
        text = request.form.get('text', None)
        subs = request.form['sub']
        write_stuff(f'\n\ntitle - {title}\ntext - {text}\nsubs - {subs}\n\n')
        return 'ok'


@app.route('/payments/')
def payments():
    pass


@app.route('/payments/success/')
def payment_success():
    pass


@app.route('/payments/fail')
def payment_fail():
    pass
