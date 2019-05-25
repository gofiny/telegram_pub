from app import app
from flask import render_template
from flask import request
from models import Subscriptions


@app.route('/')
def index():
    return render_template('main/index.html')


@app.route('/new_post/', methods=['GET', 'POST'])
def create_post():
    if request.method == 'GET':
        subs = Subscriptions.query.all()
        return render_template('main/create_post.html', subs=subs)


@app.route('/payments/')
def payments():
    pass


@app.route('/payments/success/')
def payment_success():
    pass


@app.route('/payments/fail')
def payment_fail():
    pass
