from flask import Blueprint, render_template, request, url_for, redirect, flash
from models import db, Product

shop_app = Blueprint("shop_app", __name__)


@shop_app.route("/", endpoint="home")
def main_page():
    products = Product.query.all()
    return render_template("shop_home.html", products=products)


@shop_app.route("products/confirm-delete",
                methods=["GET", "POST"],
                endpoint="confirm-delete")
@shop_app.route("products",
                methods=["GET", "DELETE"],
                endpoint="details")
def get_product(product_id: int):
    '''
    Need to insert product_id url path here (<int: product_id>)
    '''
    return render_template("index_temporary_copy.html")



