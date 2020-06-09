from flask import (Flask,render_template,jsonify,request,redirect,url_for)

##########
##Routes##
##########
from __main__ import app

@app.route("/")
def index():

    return render_template("index.html")