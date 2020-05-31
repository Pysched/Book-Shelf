import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
import bcrypt


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'bookshelf'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-46ezx.mongodb.net/bookshelf?retryWrites=true&w=majority'
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


users = mongo.db.users


def get_username(username):
    return users.find_one({"_id": str(users)})


# Home Page
@app.route('/')
@app.route('/main')
def main():
    return render_template("main.html")


# Book Club Page
@app.route('/book_club')
def book_club():
    return render_template("bookclub.html")


# Browse Page
@app.route('/browse')
def browse():
    return render_template("browse.html")


# Login Page

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'


# Sign up
@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Create new user/register new account
    Checks that the user doesn't already exist, and that length of username
    and password is between 6-15 characters
    Uses generate_password_hash to hash user's password in the database
    '''
    if request.method == "POST":

        new_username = request.form.get("new_username").lower()
        new_password = request.form.get("new_password")
        new_tagline = request.form.get("new_tagline")
        new_email = request.form.get("new_email")
        new_comment = request.form.get("new_comment")
        
        if len(new_username) < 3 or len(new_username) > 15:
            
            return redirect(url_for('register'))

        if len(new_password) < 5 or len(new_password) > 15:
          
            return redirect(url_for('register'))

        # Check if username already exists
        existing_user = get_username(new_username)
        if existing_user:
            return redirect(url_for('register'))

        # If all checks pass, add user to the database and hash the password
        users.insert_one({
            "username": new_username,
            "password": generate_password_hash(new_password),
            "tagline": new_tagline,
            "email": new_email,
            "comment": new_comment,
        })
        session["user"] = new_username

        return redirect(url_for('main', username=session["user"]))

    return render_template("register.html")


# Log out
@app.route('/logout')
def logout():
	# Clear the session
	session.clear()
	flash('You were logged out!')
	return redirect(url_for('main'))

# Profile Page
@app.route('/profile/<username>', methods=["GET", "POST"])
def profile(username): 
	# Check if user is logged in
	if 'user' in session:
		# If so get the user and pass him to template for now
		user_in_db = users.find_one({"username": users})
		return render_template('profile.html', user=user_in_db)
	else:
		flash("You must be logged in!")
		return redirect(url_for('main'))


# Add item Page
@app.route('/add_item')
def add_item():
    return render_template("additem.html")


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP', '0.0.0.0'), port=int(os.environ.get("PORT", "5000")), debug=True)