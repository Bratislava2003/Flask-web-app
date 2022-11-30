from flask import Blueprint, render_template, url_for, abort, redirect, request, g
from flask_login import login_required, current_user
from sqlalchemy import asc, desc

from models import db, User, Post
from views.forms.postform import CreatePostForm

blog_app = Blueprint("blog_app", __name__)


@blog_app.route("/", endpoint="blog_home")
def blog_home():

    cats = ["Tech", "Hardware", "Software", "Events", "News"]

    return render_template('blog_home.html', cats=cats)


@blog_app.route("/user/<string:username>/delete",methods=["GET", "POST"], endpoint="user_delete")
@blog_app.route("/user/<string:username>/posts", endpoint="user_posts")
@blog_app.route("/user/<string:username>/", methods=["GET", "DELETE"], endpoint="user_page")
def personal_page(username: str):

    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404)

    posts = request.endpoint == "blog_app.user_posts"
    user_delete = request.endpoint == "blog_app.user_delete"
    if posts:
        post_list = user.posts
        return render_template('blog_post_list.html', posts=post_list, user=user)

    if request.method == "GET":
        return render_template('blog_page.html', user=user)

    up = Post.query.filter_by(user_id=user.id).all()
    for i in up:
        db.session.delete(i)
    db.session.delete(user)
    db.session.commit()

    url = url_for("index")
    if user_delete:
        return redirect(url)

    return {"ok": True, "url": url}


@blog_app.route("/create-post", methods=["GET", "POST"], endpoint="postcr")
@login_required
def create_post():

    form = CreatePostForm()

    if request.method == "GET":
        return render_template("blog_createpost.html", form=form)

    if not form.validate_on_submit():
        return render_template("blog_createpost.html", form=form), 400

    if current_user.is_authenticated:
        g.user = current_user.get_id()

    post_title = form.title.data
    post_cat = form.category.data
    post_body = form.body.data

    post = Post(user_id=g.user, title=post_title, body=post_body, category=post_cat)  # type: ignore
    db.session.add(post)
    db.session.commit()

    url = url_for('blog_app.post', post_id=post.id)
    return redirect(url)


@blog_app.route("/post/<int:post_id>/delete/", methods=["GET", "POST"], endpoint="delete")
@blog_app.route("/post/<int:post_id>/", methods=["GET", "DELETE"], endpoint='post')
def show_post(post_id):

    post = Post.query.get_or_404(
        post_id,
        'Post not found!'
    )
    product_delete = request.endpoint == "blog_app.delete"
    if request.method == "GET":
        return render_template("blog_post.html", post=post)

    db.session.delete(post)
    db.session.commit()

    username = current_user.username

    url = url_for("blog_app.user_page", username=username)
    if product_delete:
        return redirect(url)

    return {"ok": True, "url": url}


@blog_app.route("/admin/", endpoint="admin")
def admin_panel():
    users = User.query.order_by(asc(User.username)).all()

    return render_template("blog_admin.html", users=users)


@blog_app.route("/<string:category>/", endpoint="category")
def categories(category):

    posts = Post.query.filter_by(category=category).order_by(desc(Post.created_at)).all()

    return render_template("blog_cat_page.html", posts=posts, category=category)
