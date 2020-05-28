import os
from flask import Flask, render_template, redirect, request, url_for, 
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bookshelf'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-46ezx.mongodb.net/bookshelf?retryWrites=true&w=majority'



mongo = PyMongo(app)




@app.route('/')
def index():
    return render_template("base.html")





if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'), port=int(os.environ.get("PORT")), debug=True)