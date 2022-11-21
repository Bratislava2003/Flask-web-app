from flask import Blueprint, render_template, request, url_for, redirect, flash
from models import db, User
from views.forms.login_form import CreateLoginForm

login_app = Blueprint("login_app", __name__)

@login_app.route("/", endpoint='login')
def login():
    form = CreateLoginForm()

    pass
