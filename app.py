import os
import json
from datetime import datetime
from flask_pymongo import PyMongo
from flask import Flask, render_template, request, flash, redirect, session, url_for


app = Flask(__name__)



mongo = PyMongo(app)




@app.route('/')
def index():
    return render_template("index.html")





if __name__ == '__main__':
    app.run(host=os.environ.get("IP", "0.0.0.0"),
            port=int(os.environ.get("PORT", "5000")),
            debug=True)