from app import app
from flask import render_template
from flask import request


@app.route('/')
def index():
    return render_template('main/index.html')


@app.route('/new_post/', methods=['GET', 'POST'])
def create_post():
    if request.method == 'GET':
        return render_template('main/create_post.html')


@app.route('/payments/')
def payments():
    pass


@app.route('/payments/success/')
def payment_success():
    pass


@app.route('/payments/fail')
def payment_fail():
    pass
