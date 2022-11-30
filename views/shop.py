from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required
from models import db, Product
from views.forms.prod_form import CreateProductForm

shop_app = Blueprint("shop_app", __name__)


@shop_app.route("/", endpoint="home")
def main_page():
    products = Product.query.order_by(Product.id).all()
    return render_template("shop_home.html", products=products)


@shop_app.route("/<int:product_id>/confirm-delete/",
                methods=["GET", "POST"],
                endpoint="confirm-delete")
@shop_app.route("/<int:product_id>/",
                methods=["GET", "DELETE"],
                endpoint="details")
def get_product(product_id: int):
    product: Product = Product.query.get_or_404(
        product_id,
        f"Product #{product_id} not found! "
    )
    confirm_delete = request.endpoint == "products_app.confirm-delete"
    if request.method == "GET":
        return render_template("shop_details.html", product=product)

    db.session.delete(product)
    db.session.commit()

    url = url_for("shop_app.home")
    if confirm_delete:
        return redirect('url')

    return {"ok": True, "url": url}


@shop_app.route("/add/", methods=["GET", "POST"], endpoint="add")
@login_required
def add_product():

    form = CreateProductForm()

    if request.method == "GET":
        return render_template("shop_add.html", form=form)

    if not form.validate_on_submit():
        return render_template("shop_add.html", form=form), 400

    product_name = form.name.data
    product_type = form.product_type.data
    product_description = form.product_description.data

    product = Product(name=product_name, prod_type=product_type, description=product_description)
    db.session.add(product)
    db.session.commit()

    url = url_for("shop_app.details", product_id=product.id)
    return redirect(url)
