import os
from app import create_app, db
from app.models import User
from flask_migrate import Migrate
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app,db)

with app.app_context():
    db.create_all()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)