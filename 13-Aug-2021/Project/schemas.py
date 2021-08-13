from flask_wtf import FlaskForm
from wtforms import FloatField,SubmitField
from wtforms.validators import DataRequired

class Form(FlaskForm):
    p = FloatField('Phosphorous',validators=[DataRequired()])
    k = FloatField('Potassium',validators=[DataRequired()])
    n = FloatField('Nitrogen',validators=[DataRequired()])
    temp = FloatField('Temperature in degree',validators=[DataRequired()])
    humi = FloatField('Humidity in %',validators=[DataRequired()])
    ph = FloatField('pH value',validators=[DataRequired()])
    rain = FloatField('Rainfall in mm',validators=[DataRequired()])

    submit = SubmitField('Submit')