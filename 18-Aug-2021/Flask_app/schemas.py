from flask_wtf import FlaskForm
from wtforms import FloatField,SubmitField,DateField,SelectField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired
import pickle, sklearn
from datetime import datetime
import numpy as np

# regression algorithm pickle files
brand_encode = pickle.load(open('pickle_files_regre/brand.pkl','rb'))
fuel_encode = pickle.load(open('pickle_files_regre/fuel.pkl','rb'))
owner_encode = pickle.load(open('pickle_files_regre/owner.pkl','rb'))
seller_encode = pickle.load(open('pickle_files_regre/seller.pkl','rb'))
trans_encode = pickle.load(open('pickle_files_regre/transmission.pkl','rb'))
scalar_regre = pickle.load(open('pickle_files_regre/scalar.pkl','rb'))
regressor = pickle.load(open('pickle_files_regre/decision_tree.pkl','rb'))

# classification algorithm pickle files
classifier = pickle.load(open('pickle_files_class/classifier.pkl','rb'))
scalar = pickle.load(open('pickle_files_class/scalar.pkl','rb'))
encoder = pickle.load(open('pickle_files_class/encoder.pkl','rb'))


class Classi_Form(FlaskForm):
    p = FloatField('Phosphorous',validators=[DataRequired()])
    k = FloatField('Potassium',validators=[DataRequired()])
    n = FloatField('Nitrogen',validators=[DataRequired()])
    temp = FloatField('Temperature in degree',validators=[DataRequired()])
    humi = FloatField('Humidity in %',validators=[DataRequired()])
    ph = FloatField('pH value',validators=[DataRequired()])
    rain = FloatField('Rainfall in mm',validators=[DataRequired()])

    submit = SubmitField('Submit')

class Regree_Form(FlaskForm):
    date = DateField('Registration Year (YYYY)',format='%Y')
    brand = SelectField('Brand',choices=brand_encode.classes_)
    km = IntegerField('Kilometer')
    fuel = SelectField('Fuel Type',choices=fuel_encode.classes_)
    seller = SelectField('Seller Type',choices=seller_encode.classes_)
    transmission = SelectField('Transmission',choices=trans_encode.classes_)
    owner = SelectField('Owner type', choices=owner_encode.classes_)
    seats = IntegerField('No. of Seats')
    milage = FloatField('Milage in kmpl')
    engine = IntegerField('Engine CC')

    submit = SubmitField('Submit')


# defining function to get the results
def classification_model(p,k,n,temp,humi,ph,rain):
    scaled_data = scalar.transform([[p,k,n,temp,humi,ph,rain]])
    return encoder.classes_[int(classifier.predict(scaled_data))]

# defining function for getting results of regression model
def regression_model(Date,brand,km,fuel,seller,trans,owner,seat,milage,cc):
    year = Date.year
    brand = int(brand_encode.transform([brand]))
    seller = int(seller_encode.transform([seller]))
    transmission = int(trans_encode.transform([trans]))
    fuel = int(fuel_encode.transform([fuel]))
    owner = int(owner_encode.transform([owner]))

    # calculating the age of the vehicle
    age = datetime.now().year - year

    scaled_data = scalar_regre.transform([[km,fuel,seller,transmission,owner,seat,brand,milage,cc,age]])

    result = np.exp(regressor.predict(scaled_data))

    return result