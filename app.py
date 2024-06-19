from flask import Flask, render_template
from admin import admin_bp, db, bcrypt, login_manager
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
app.secret_key = "pineapple"

# Construct the path to the database
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(base_dir, 'admin', 'instance', 'login.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
bootstrap = Bootstrap5(app)

# Register blueprint
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route("/")
def my_home():
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create the database and tables
    app.run(debug=True)
