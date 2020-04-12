from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://eelxygymmyyfol:0d72aada4bce21ebb6347e6ad6d09b5abfc7f2d1a43c051d22730c7cd92412d3@ec2-18-215-99-63.compute-1.amazonaws.com:5432/d1in0i6b8fj806"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)
db.init_app(app)
Migrate(app, db)

UPLOAD_FOLDER = "./app/static/upload"

app.config.from_object(__name__)
from app import views
