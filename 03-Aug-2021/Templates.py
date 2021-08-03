### importing flask library
from flask import Flask, render_template

### Application instant
app = Flask(__name__)

### defining decorators
@app.route('/')
def index():        ### defining function
    return render_template('index.html')       ### retuning the string 

@app.route('/<name>')
def user(name):
    return render_template('user.html',name=name)