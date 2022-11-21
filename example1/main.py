
from flask import Flask, request, render_template, make_response, redirect

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

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
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    #app.run(debug=True)
    #app.run()