from flask_wtf import FlaskForm
from wtforms import FloatField,SubmitField,DateField,SelectField
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired
import pickle, sklearn

# regression algorithm pickle files
brand = pickle.load(open('pickle_files_regre/brand.pkl','rb'))
fuel = pickle.load(open('pickle_files_regre/fuel_type.pkl','rb'))
gear = pickle.load(open('pickle_files_regre/gearbox.pkl','rb'))
repair = pickle.load(open('pickle_files_regre/repair.pkl','rb'))
vehicle_type = pickle.load(open('pickle_files_regre/vehicle_type.pkl','rb'))

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
    date = DateField('Registration Date',validators=[DataRequired()],format='%Y-%m')
    vtype = SelectField('Vehicle Type',choices=vehicle_type.classes_)
    gear = SelectField('Gear Box',choices=gear.classes_)
    km = IntegerField('Kilometer',validators=[DataRequired()])
    fuel = SelectField('Fuel Type',choices=fuel.classes_)
    brand = SelectField('Vehicle Brand', choices=brand.classes_)
    repair = SelectField('Is vehicle repaired...?',choices=repair.classes_)

    submit = SubmitField('Submit')


# defining function to get the results
def classification_model(p,k,n,temp,humi,ph,rain):
    scaled_data = scalar.transform([[p,k,n,temp,humi,ph,rain]])
    return encoder.classes_[int(classifier.predict(scaled_data))]