from flask import Flask, render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from wtforms import Form, StringField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "pineapple"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)