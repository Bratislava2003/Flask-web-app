from flask import Flask, render_template, redirect, url_for, flash
from flask_migrate import Migrate
from sqlalchemy import desc
import db_cfg
from views.blog import blog_app
from views.shop import shop_app
from views.forms.login_form import login_form
from views.forms.register_form import reg_form
from models import db, User, Post
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_bcrypt import Bcrypt, check_password_hash
from waitress import serve

app = Flask(__name__)
login_manager = LoginManager()
bc = Bcrypt()

app.config.update(
    SECRET_KEY="asdfasd",
    SQLALCHEMY_DATABASE_URI=db_cfg.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=db_cfg.SQLALCHEMY_TRACK_MODIFICATIONS
)

db.init_app(app)
migrate = Migrate(app, db)
bc.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
db.app = app

app.register_blueprint(shop_app, url_prefix="/shop")
app.register_blueprint(blog_app, url_prefix="/blog")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', endpoint='index')
def hello_world():

    articles = Post.query.order_by(desc(Post.created_at)).slice(0, 6).all()

    return render_template('index.html', articles=articles)


@app.route("/login/", methods=['GET', 'POST'], endpoint="login")
def login():
    form = login_form()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if check_password_hash(user.pwd, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        flash("Invalid Username/Password")

    return render_template("login.html", form=form)


@app.route("/register/", methods=['GET', 'POST'], endpoint='register')
def register():
    form = reg_form()

    if form.validate_on_submit():
        var_username = form.username.data
        var_email = form.email.data
        var_pwd = bc.generate_password_hash(form.password.data).decode('utf-8')
        print(var_pwd)

        new_user = User(username=var_username, email=var_email, pwd=var_pwd)  # type: ignore
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template("login.html", form=form)


@app.route("/logout/", endpoint="logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/about/', endpoint='about')
def text():
    return render_template('about.html')


if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=8080)
