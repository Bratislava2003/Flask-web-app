from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length


class CreateProductForm(FlaskForm):
    name = StringField(
        label="Product name",
        name="product-name",
        validators=[
            DataRequired(),
            Length(min=3, max=80),
        ],
    )
    product_type = SelectField(
        'Select type',
        name="product-type",
        choices=[("", "Select..."),
                 ("GPU", "GPU"),
                 ("CPU", "CPU"),
                 ("RAM", "RAM"),
                 ("Motherboard", "Motherboard"),
                 ("CPU Cooler", "CPU Cooler"),
                 ("Fan", "Fan"),
                 ("Cable", "Cable"),
                 ("Misc.", "Misc."),
                 ("Case", "Case"),
                 ("Monitor", "Monitor"),
                 ("Keyboard", "Keyboard"),
                 ("Mouse", "Mouse"),
                 ],
        validators=[
            DataRequired()
        ],
    )
    product_description = StringField(
        label="Product description",
        name="product-description",
        validators=[
            DataRequired(),
            Length(max=300),
        ],
    )
