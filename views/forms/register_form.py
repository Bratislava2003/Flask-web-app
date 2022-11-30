from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import Length, InputRequired, Email, Regexp, EqualTo, ValidationError

from models import User


class reg_form(FlaskForm):
    username = StringField(validators=[InputRequired(),
                                      Length(3, 25, message="Input your name"),
                                      Regexp("^[A-Za-z][A-Za-z0-9_.]*$",
                                             0,
                                             "Try letters A-Z, a-z, simple numbers... Okay, dot and underscore too)")
                                      ])
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField(validators=[InputRequired(), Length(8, 24)])
    validate_pass = PasswordField(validators=[InputRequired(),
                                              Length(8, 24),
                                              EqualTo("password", message="You can't type in 1 line 2 times in a row?)")
                                              ])

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Existing email. Not a surprise. It would be if it were aliens")

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("Already taken, you are not the only genius)")
