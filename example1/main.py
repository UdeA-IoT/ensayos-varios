
from flask import Flask, request, render_template, make_response, redirect

app = Flask(__name__)

@app.route('/')
def index():
    
    #response = make_response(redirect('/index'))
    response = render_template('base.html')
    return response

@app.route('/index')
def home():
    context = {
        'client_ip': request.remote_addr
    }
    return render_template('index.html', **context)
    
