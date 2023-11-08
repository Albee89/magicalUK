from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

def BasicForm():
    ids = StringField("ID",validators=[DataRequired()])
    submit = SubmitField("Submit")

