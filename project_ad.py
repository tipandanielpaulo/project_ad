# -*- coding: utf-8 -*-
"""
Created on Wed May 27 12:04:27 2020
@author: Paulo
Project Area Denial
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


from flask import Flask, redirect, url_for, render_template, request, Response


app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/members")
def members():
    """Members Page"""
    return render_template("members.html")

@app.route("/about")
def about():
    """About Page"""
    return render_template("about.html")


@app.route("/data")
def data():
    df = pd.read_csv('Stat/covid.csv')
    return render_template('data.html',  tables=[df.to_html(classes='data')])



@app.route("/no_page")
def no_page():
    """Redirect page"""
    return "<h1>The website you are looking for is not found.<h1>"
    
@app.route("/<name>")
def user(name):
    """This is for <name> or mispelled webpages"""
    return redirect(url_for("no_page"))



if __name__ == "__main__":
        app.run(debug=True)