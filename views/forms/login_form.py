from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, StopValidation
from models.database import db
from models.user import User


class UserDbValidate():

    def __init__(self, message=None):
        self.message = message
        self.field_flags = {"required": True}

    def __call__(self, form, field):
        user_request = User.query.get_or_404(
            field.data
        )
        if user_request != 404:
            return
        raise StopValidation(message="User not found!")


class CreateLoginForm(FlaskForm):
    login_field = StringField(
        label="Login",
        name="login",
        validators=[
            DataRequired(),
            UserDbValidate()
        ],
    )
    password_field = StringField(
        label="Password",
        name="password",
        validators=[
            DataRequired(),
            UserDbValidate()
        ]
    )
