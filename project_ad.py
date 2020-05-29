# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:04:27 2020
@author: Team Phi - 6
Project Area Denial
"""

# Flask
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    """Home Page"""
    return render_template("index.html")

@app.route("/members")
def members():
    """Members Page"""
    return render_template("members.html")

@app.route("/about")
def about():
    """About Page"""
    return render_template("about.html")

@app.route("/reference")
def reference():
    """Reference Page"""
    return render_template("reference.html")


@app.route("/data")
def data():
    """Answer Page"""
    return render_template('data.html')




@app.route("/no_page")
def no_page():
    """Redirect page"""
    return "<h1>The website you are looking for is not found.<h1>"
    
@app.route("/<name>")
def user(name):
    """This is for <name> or mispelled webpages"""
    return redirect(url_for("no_page"))


#Flask
if __name__ == "__main__":
        app.run(debug=True)