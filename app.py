import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, flash, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)


# Add Databse
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(app)

# Loading secret-key
load_dotenv()
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


# Create Model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    data_added = db.Column(db.DateTime, default=datetime.utcnow)

    # Create A String
    def __repr__(self):
        return "<Name %r>" % self.name


# Create a form class
class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[Email()])
    submit = SubmitField("submit")


# create a form class
class NamerForm(FlaskForm):
    name = StringField("whats your name? ", validators=[DataRequired()])
    submit = SubmitField("submit")


# create a route decorator
@app.route("/")
def index():
    first_name = "john"
    stuff = "This is <strong>Bold</strong>"
    favourite_pizza = ["pepporoni", "cheeze", "garlic", 41]

    return render_template(
        "index.html",
        first_name=first_name,
        stuff=stuff,
        favourite_pizza=favourite_pizza,
    )


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


# create custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal server error
@app.errorhandler(500)
def server_error(e):
    return render_template("404.html"), 500


# create name page
@app.route("/name", methods=["GET", "POST"])
def name():
    name = None
    form = NamerForm()

    # validation stufff
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Form Submitted Sucessfully")
    return render_template("name.html", name=name, form=form)


@app.route("/user/add", methods=["GET", "POST"])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ""
        form.email.data = ""
        flash("User Added Successfully!")

    our_users = Users.query.order_by(Users.data_added)
    return render_template("add_user.html", name=name, form=form, our_users=our_users)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
