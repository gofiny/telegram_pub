from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('main/index.html')


@app.route('/payments/')
def payments():
    pass


@app.route('/payments/success/')
def payment_success():
    pass


@app.route('/payments/fail')
def payment_fail():
    pass
