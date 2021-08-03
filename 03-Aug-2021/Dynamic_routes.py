### importing flask library
from flask import Flask, redirect

### Application instant
app = Flask(__name__)

### defining decorators
@app.route('/')
def index():        ### defining function
    return '<h1>Hi, Welcome</h1>'       ### retuning the string 

@app.route('/user/<name>')
def user(name):
    return '<h1>Hi {} </h1>'.format(name)

@app.route('/redirect')
def redirect():
    return redirect('https://www.wowlabz.com/')