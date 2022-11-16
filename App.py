from flask import Flask, render_template
from flask_migrate import Migrate
import db_cfg
from views.shop import shop_app
from models import db, User, Post
from jsonapi.main import get_list

app = Flask(__name__)


app.config.update(
    SECRET_KEY="asdfasd",
    SQLALCHEMY_DATABASE_URI=db_cfg.SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=db_cfg.SQLALCHEMY_TRACK_MODIFICATIONS
)

db.app = app
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(shop_app, url_prefix="/shop")


def add_json_ph():
    reformed_list = get_list()

    names = reformed_list[0]
    usernames = reformed_list[1]
    emails = reformed_list[2]

    bodies = reformed_list[5]
    titles = reformed_list[4]
    user_ids = reformed_list[3]

    with app.app_context():

        for i in range(len(reformed_list[0])):
            user = User(user_name=names[i], username=usernames[i], email=emails[i])
            db.session.add(user)
        db.session.commit()

        for k in range(len(reformed_list[3])):
            post = Post(user_id=user_ids[k], title=titles[k], body=bodies[k])
            db.session.add(post)
        db.session.commit()


@app.route('/', endpoint='index')
def hello_world():
    return render_template('index.html')


@app.route('/about/', endpoint='about')
def text():
    return render_template('about.html')


if __name__ == '__main__':
    add_json_ph()
    app.run(debug=True)
