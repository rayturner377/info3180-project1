from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://lbmkizyoaccchu:a0c8fa193e9da2213959d93f5a5f3e415b9bf85eec418585c4ac3f7e85c6158b@ec2-34-193-232-231.compute-1.amazonaws.com:5432/d4jp4rhid4o5m6"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)
db.init_app(app)
Migrate(app, db)

UPLOAD_FOLDER = "./app/static/upload"

app.config.from_object(__name__)
from app import views
