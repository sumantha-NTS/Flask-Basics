from flask import Flask,render_template
from flask.helpers import flash
from flask_bootstrap import Bootstrap
from schemas import Classi_Form,Regree_Form,classification_model, regression_model


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = "sample project"

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/classification',methods=['GET','POST'])
def classification():
    form = Classi_Form()
    if form.validate_on_submit():
        p = form.p.data
        k = form.k.data
        n = form.n.data
        temp = form.temp.data
        humi = form.humi.data
        ph = form.ph.data
        rain = form.rain.data

        result = classification_model(p,k,n,temp,humi,ph,rain)
        flash(f'Predicted Crop is {result.upper()}')
    return render_template('classification.html',form = form)

@app.route('/Regression',methods=['GET','POST'])
def regression():
    form = Regree_Form()
    if form.validate_on_submit():
        date = form.date.data
        brand = form.brand.data
        km = form.km.data
        fuel = form.fuel.data
        seller = form.seller.data
        trans = form.transmission.data
        owner = form.owner.data
        seat = form.seats.data
        milage = form.milage.data
        cc = form.engine.data

        result = regression_model(date,brand,km,fuel,seller,trans,owner,seat,milage,cc)
        flash(result)

    return render_template('regression.html',form=form)



if __name__ == "__main__":
    app.run(debug=True)