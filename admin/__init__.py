from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

admin_bp = Blueprint('admin', __name__, static_folder='static', template_folder='templates', url_prefix='/admin')

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from .models.user import User
    return db.get_or_404(User, user_id)

# Ensure the import path is correct based on the project structure
from .routes import main_routes