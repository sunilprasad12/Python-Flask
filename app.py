from flask import Flask, render_template, url_for, flash, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from models import User, Post




@app.route("/")
def home():
    return render_template("PerfectMatchWeb.html")



@app.route("/PhotoGrid.html")
def gallary():
    return render_template("PhotoGrid.html")

@app.route("/Webpage.html")
def about():
    return render_template("Webpage.html")

@app.route("/CompleteRegistertionform.html")
def singup():
     return render_template("CompleteRegistertionform.html")

@app.route("/Aboutme.html")
def contact():
     return render_template("Aboutme.html")


if __name__ == "__main__":
    app.run(debug=True)


