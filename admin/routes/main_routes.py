from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from .. import admin_bp, db
from ..models.user import User
from ..forms.admin_forms import LoginForm, SignupForm

@admin_bp.route("/", methods=["GET", "POST"])
def home():
    if current_user.is_authenticated:
        flash("You are already logged in!")
        return redirect(url_for("admin.user"))
    my_form = LoginForm()
    if my_form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == my_form.email.data)).scalar()
        if user and user.verify_password(my_form.password.data):
            login_user(user)
            flash("You are successfully logged in!")
            return redirect(url_for("admin.user"))
        flash("Invalid username or password")
    return render_template("login.html", form=my_form)

@admin_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        flash("You are already signed in!")
        return redirect(url_for("admin.user"))
    my_form = SignupForm()
    if my_form.validate_on_submit():
        user = User.query.filter_by(email=my_form.email.data).first()
        if user:
            flash("Email already exists!")
            return redirect(url_for("admin.signup"))
        user = User(username=my_form.username.data, email=my_form.email.data)
        user.password = my_form.password.data
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash("You have successfully registered and logged in!")
        return redirect(url_for("admin.user"))
    return render_template("register.html", form=my_form)

@admin_bp.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("You logged out successfully!")
    return redirect(url_for("admin.home"))

@admin_bp.route("/user")
def user():
    if current_user.is_authenticated:
        users = User.query.all()
        return render_template("user.html", user=current_user.username, data=users)
    flash("You must login first!")
    return redirect(url_for("admin.home"))