from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = "hard to guess string"

class Nameform(FlaskForm):
    name = StringField('What is your name..?',validators=[DataRequired()])
    location = StringField('Your Location')
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    location = None
    form = Nameform()
    if form.validate_on_submit():
        name = form.name.data
        location = form.location.data
        form.name.data = ''
    return render_template('index.html',form = form, name=name)