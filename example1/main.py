
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    client_ip = request.remote_addr
    # return 'Hello, World! to {}'.format(client_ip)
    return render_template("hello.html", client_ip = client_ip)
