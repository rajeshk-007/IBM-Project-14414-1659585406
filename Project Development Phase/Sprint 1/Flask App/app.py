rom flask import Flask,render_template,redirect
from flask import url_for,session,request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
import hashlib
import re
import ibm_db

app = Flask(__name__)
app.secret_key = os.urandom(16)

try:
    conn = ibm_db.connect(os.getenv('CREDENTIALS'),'','')
except Exception as err:
     print("Exception occurs->", err)



@app.route('/')
def index():
    if not session or not session['login_status']:
        return render_template('index.htm')

    return redirect(url_for('home'))



@app.route('/login')
def login():
    if not session or not session['login_status']:
        return render_template('login.htm')

    return redirect(url_for('home'))


@app.route('/register')
def register():
    if not session or not session['login_status']:
        return render_template('register.htm')

    return redirect(url_for('home'))




@app.route('/home')
def home():
    if not session:
        return redirect(url_for('login'))

    if session['login_status']:
        return render_template('home.htm',username=session['user_id'])

    return redirect(url_for('login'))

