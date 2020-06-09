#Import Modules for Flask Server to Run

from flask import (Flask,render_template,jsonify,request,redirect,url_for)
import pandas as pd
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

##Flask Setup
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

##Import Database Variables to connect to Local PostgreSQL database.
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost/fuelly"
db = SQLAlchemy(app)
# from .models import fuellytable
Base = automap_base()
Base.prepare(db.engine, reflect=True)

#Statement to run to show databased has connected locally.
print("Database is now connected")

#import our routes from extra file
import app_routes

#Set Flask App debugging to true.
if __name__ == "__main__":
    app.run(debug=True)