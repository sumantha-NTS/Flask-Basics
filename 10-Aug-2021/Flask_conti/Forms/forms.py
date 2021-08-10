from flask import Flask, render_template, redirect, session, url_for
from flask.helpers import flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = "hard to guess string"

### creating class for form
class Nameform(FlaskForm):
    name = StringField('What is your name..?',validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form = Nameform()      ## calling the form class and initiating to form varible 
    if form.validate_on_submit():
        old_name = session.get('name')
        if (old_name is not None) and (old_name!=form.name.data):       ## just to flash a message
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data        ### getting the name data
        flash('Nice name!!!')
        return redirect(url_for('index'))       ### redirecting to index function again
    return render_template('index.html',form = form, name=session.get('name')) 

if __name__ == '__main__':
    app.run(debug=True)