from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length


class CreatePostForm(FlaskForm):
    category = SelectField(
        'Select category',
        name="title-category",
        choices=[("", "Select..."),
                 ("Tech", "Tech"),
                 ("Hardware", "Hardware"),
                 ("Software", "Software"),
                 ("Events", "Events"),
                 ("News", "News"),
                 ],
        validators=[
            DataRequired()
        ],
    )
    title = StringField(
        "Title",
        name="title",
        validators=[
            DataRequired(),
            Length(min=5, max=30)
        ]
    )
    body = TextAreaField(
        "Body",
        name="body",
        validators=[
            DataRequired(),
            Length(min=5, max=300)
        ]
    )
