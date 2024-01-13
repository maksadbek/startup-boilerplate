import time

from flask import (
    Flask,
    render_template,
    request,
    flash,
    make_response,
    redirect,
    url_for,
    session,
)

from flask_login import LoginManager, login_user, current_user, login_required, AnonymousUserMixin
from flask_migrate import Migrate

from app.database.sqlite import db
from app.forms.login import LoginForm
from app.forms.signup import SignupForm
from app.forms.item import ItemForm
from app.models import user, item
import sqlalchemy as sa
import sqlalchemy.orm as so

import uuid

app = Flask(__name__, template_folder="../templates")
app.config.from_object("app.config.local.Config")

login = LoginManager(app)
login.login_view = 'login'
# login.anonymous_user = user.AnonymousUser

# print(app.config)
db.init_app(app)

migrate = Migrate(app, db)


ANONYMOUS_ID = "_anonymous_id"


@login.user_loader
def load_user(user_id):
    if ANONYMOUS_ID in session:
        return user.AnonymousUser(session[ANONYMOUS_ID])

    return db.session.get(user.User, int(user_id))


@app.before_request
def assign_unique_id():
    if not current_user.is_authenticated:
        if ANONYMOUS_ID not in session:
            session[ANONYMOUS_ID] = str(uuid.uuid4())

            login_user(user.AnonymousUser(session[ANONYMOUS_ID]), force=True)


@app.route("/")
@login_required
def index():
    return render_template("index.html", user=current_user)


@app.route("/x/clicked")
def clicked():
    resp = f"<p>Hello World! {repr(current_user)}</p>"

    return resp


@app.route("/stream")
def stream():
    def generate():
        for i in range(100000):
            time.sleep(1)
            yield "hello"

    return generate(), {"Content-type": "text/text"}


@app.route("/login", methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        u = db.session.scalar(sa.select(user.User).where(user.User.username == form.username.data))

        if u is None or not u.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(u, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form, anonymous_id=current_user.id)


@app.route("/signup", methods=('GET', 'POST'))
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = SignupForm()

    if form.validate_on_submit():
        u = user.User(username=form.username.data, email=form.email.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')

        return redirect(url_for('login'))

    return render_template("signup.html", title='Register', form=form)


@app.route("/items", methods=("GET", "POST"))
def items():
    form = ItemForm()

    if form.validate_on_submit():
        it = item.Item(
            title=form.title.data,
            description=form.description.data,
            price=form.price.data,
            active=False,
        )

        db.session.add(it)
        db.session.commit()

        return render_template("item.html", item=it)

    records = db.session.execute(sa.select(item.Item)).all()

    return render_template("items.html", items=records, form=form)


if __name__ == '__main__':
    app.run()
