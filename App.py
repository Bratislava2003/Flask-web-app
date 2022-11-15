from flask import Flask, render_template
from flask_migrate import Migrate
import db_cfg
from views.shop import shop_app
from models import db

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


@app.route('/', endpoint='index')
def hello_world():
    return render_template('index.html')


@app.route('/about/', endpoint='about')
def text():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
