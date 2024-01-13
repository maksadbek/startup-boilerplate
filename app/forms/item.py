from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class ItemForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = PasswordField("description", validators=[DataRequired()])
    price = IntegerField("Price")
    submit = SubmitField("Sign In")
