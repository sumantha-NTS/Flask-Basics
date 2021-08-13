from flask import Flask,render_template
from flask.helpers import flash
from flask_bootstrap import Bootstrap
from schemas import Form

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = "sample project"

@app.route('/',methods=['GET','POST'])
def index():
    form = Form()
    if form.validate_on_submit():
        p = form.p
    return render_template('index.html',form = form)

@app.route('/details')
def details():
    return 'yet to furnish...'

if __name__ == "__main__":
    app.run(debug=True)