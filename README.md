# [Book Shelf]() - Milestone Project Three

## Table of Contents

- [**About**](#About)
  - [Why This Project?](#Why-This-Project)
- [**UX**](#UX)
  - [User Stories](#User-Stories)
  - [Style Development](#Style-Development)
  - [Wireframes](#Wireframes)
  - [Database Schema](#Database-Schema)
- [**Features**](#Features)
  - [Functionality](#Functionality)
  - [Existing Features](#Existing-Features)
  - [Features Left To Implement](#Features-Left-To-Implement)
- [**Technologies Used**](#Technologies-Used)
  - [Version Control](#Version-Control)
  - [Hosting](#Hosting)
- [**Testing**](#Testing)
  - [Testing User Stories](#Testing-User-Stories)
  - [Responsive and Functional Testing](#Responsive-and-Functional-Testing)
  - [Additional Testing](#Additional-Testing)
  - [Code Validation](#Code-Validation)
  - [Interesting Bugs Or Problems](#Interesting-Bugs-Or-Problems)
    - [Resolved Bugs](#Resolved-Bugs)
    - [Partially Resolved or Unresolved Bugs](#Partially-Resolved-or-Unresolved-Bugs)
- [**Deployment**](#Deployment)
  - [Live App Link](#Live-App-Link)
  - [Repository Link](#Repository-Link)
  - [Running Code Locally](#Running-Code-Locally)
- [**Credits**](#Credits)
  - [Content](#Content)
  - [Acknowledgements](#Acknowledgements)
  - [Disclaimer](#Disclaimer)

## About

Book Shelf is an web application, designed as a great place for avid book lovers, page turners, friendly discussion and a facility to aid users to buy books. The aims of the site are to be a central location for people who want to read reviews by fellow book enthusists, join a bookclub group, arrange online meeting times for healthy discussion and as a place where they can link to buy the books they want. 

Users will be able to create reviews about their favourite books, like and vote on other books reviewed by other people.
Users can also create their own free account and add reviews that they can share with other users and visitors.

A free to join site that brings people together and allows them to share their passion and buy books.

### Why This Project?

This app was created for the Data Centric Development project of [**_Code Institute's_**](https://codeinstitute.net/) Full Stack Software Development course. The project scope was to create a web app using Python and a no-SQL database (MongoDB), which uses **CRUD** operations to allow users to easily create, read, update and delete data from a databse viewed through a web application

This was developed as both a front-end and backend project. The technologies used for each are:
- Frontend: HTML, CSS, JavaScript
- Backend: Python, Flask, MongoDB
- Hosting: Heroku
- Database: MongoDB

## UX

### User Stories

- As an avid reader of books, I often find myself on the look out for my enxt book and would like a place that can provide reviews on books not based from a seller site
- As a reader of books who enjoys discussing books i read, i would like to find a community that I can join to talk about books online and where I can organise meetings
- As a busy person I want to find a site where I can find reviews that are not related to a marketing stragey and are based on person opinions
- As a new reader I want to search books in an easy to navigate manner where I can link to a seller site 
- As a community member I want a place where I can store recommendations from other users
- As a reader I want to leave a rating and or a review of books I've read without taking part in anything else
- As a blogger, I want to be able to rate recipes that I try out so that I can let others know how good/bad they are
- As a consumer, I want to be able to search for a particular genre by category, release date, reviews and ratings
- As a consumer, I want to be able to use a site that is not a direct seller and is not bias towards any one book, publisher or author, in particular
- As a consumer, I want to see a summary list of books based on the most liked, so that I can quickly see the most popular ones

### Style Development



### Wireframes

Wireframes where developed using Balsamiq. These have been developed from a mobile first perspective so that every feature is designed from the smallest up, rather than desigined to fit everything in afterwards.
The site is designed to be responsive. 

The links to the files are below:


### Database Schema

I designed a databse schema before starting my project, the layout for these are available below:

## Features

### Functionality

This app makes use of Python logic to enable users to login and, or register for an account. 
The CRUD features that are available through using Python and Mongodb allow users to create, read, update and delete records in a variety of manners:

- Create book listing
- Create a favourite list
- Create a book review
- Create a book rating
- Create a book club meeting
- Read their book listings
- Read book reviews
- Read their favourites list
- Read/view book ratings by all users
- Read reviews by other users
- Read Book Club meetings 
- Read book listings by category
- Update their listings
- Update their reviews
- Update their favourites list
- Update a book rating
- Update a book club meeting
- Delete their own book listing
- Delete their own book review
- Delete their own favourite listings items
- Delete book Club meetings
- Delete their user account


### Proposed Features

-**Navbar Links** 
The navbar will contain the following links to all users:

-- Branding Icon( Also home button )
-- Home Button
-- Book Club button
-- Browse Categories dropdown( Genre, Reviews, Releases, Book of the month ) 
-- Login
-- Register

When the user is registered and logged, the navbar will add Account and log out to the navbar and remove login and register buttons from the UI

The account button will consist of the following options in a dropdown:
- Peronal information
- Add/edit/remove a new Review
- Add/edit/remove a new book listing

- **Login** - Place for previously registered users to login to their account. 
The form's username field only accepts alphanumeric values. Authorization checks are used to verify the username and password ( password is hashed ) with the details checked against the stored varibles in the database before users are logged in.

- **Register** - facility to allow new users to register for an account. The form's username field only accepts alphanumeric values. Checks are in place to ensure that the username doesn't already exist in the database before users are successfully registered. The passwords stored in the database are hashed for security purposes.

- **Logout** - Allows users to logout of their account by clicking the 'Logout' link in the navbar. Upon clicking the button, the user session ends.

- **Add Book Listing** 

- **Liked Book List** 

- **Change Password** 

- **Delete Account** 

- **Browse** 

- **Search**

- **Filter** 

- **Reset Button** 

- **Pagination** 

- **Add Review** 

- **Add New Book Club Meeting** 

- **Remove Book Listing** 

- **Remove Book Review** 

- **Cancel Button (Add Book, Review, Listing Page)** - Cancels the form submission when clicked and redirects the user to the Home page.

- **Rate Book** - The Rate It button is only available if the user is logged in. Clicking the Rate It button triggers the Rate It modal. The modal has a dropdown menu from which the user can select their rating. The user can't submit the form without selecting an option. Upon form submission, the rating value is converted to an integer and is added to the recipe record's 'rating_values' list in the database, and the new average rating value and rating count are calculated and displayed on the webpage.

- **Like Book** - The Like button is only available if the user is logged in. Clicking the Like button adds the recipe's ObjectID to the user's liked recipes list in the database, the button icon is filled in and the text changes to 'Liked'.

- **Unlike Book** - The Liked button is only available if the user is logged in and has already liked the recipe. Clicking the button removes the recipe's ObjectID from the user's liked recipes list in the database, the button icon is no longer filled in and the text changes back to 'Like'. The user can do this from the recipe page, or from their liked list in their Profile page.

- **Custom Error Messages**

### Features Left to Implement



## Technologies Used

- [**Balsamiq**](https://balsamiq.com/)
    - I've used **Balsamiq** to create wireframes of my website/app before building it.
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my app.
- [**Materialize**](https://materializecss.com/)
    - The project uses the **Materialize** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Materialize styles to my app, before adding my custom styles.
- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** as the primary JavaScript functionality. This is both the standard jQuery that is built with Materialize components, and my custom jQuery used in my script.js file.
- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.
- [**PyMongo**](https://api.mongodb.com/python/current/)
    - The project uses **PyMongo** as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.
- [**Flask**](https://flask.palletsprojects.com/en/1.0.x/)
    - The project uses **Flask**, which is a Python microframework.
- [**Flask Blueprint**](https://flask.palletsprojects.com/en/1.0.x/blueprints/)
    - The project user **Flask Blueprint** to compartmentalise my Python code and make it more modular and easier to navigate.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Flask in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
- [**MongoDB**](https://cloud.mongodb.com/)
    - The project uses **MongoDB** to store the database in the cloud. The information displayed in the front-end app is pulled from the database store.
- [**Google Fonts**](https://fonts.google.com/)
    - The project uses **Google Fonts** to style the text and suit my chosen theme. The brand logo uses the *_Dancing Script_* font and the rest of the site uses the *_Roboto_* font.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the various icons in my app.
- [**AWS Educate Cloud9**](https://aws.amazon.com/education/awseducate/)
    - I've used **AWS Educate Cloud9** as the development environment to write the code for my website.

### Version Control

- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to project in AWS Educate Cloud9, before pushing them to GitHub.
- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.

### Hosting
- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.

## Testing

### Testing User Stories


### Responsive and Functional Testing


### Additional Testing


### Code Validation

- I will use the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
- I will use the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I will use the [Esprima Syntax Validator tool](http://esprima.org/demo/validate.html) to validate my JavaScript syntax.
- I will use the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.

## Deployment

I used GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, I used the following steps:

1. Created the app in Heroku.
2. Ran the `sudo snap install --classic heroku` command in the terminal window to instal heroku in my local workspace.
3. Ran the `heroku login --interactive` command in the terminal window and entered my credentials to login to Heroku.
4. Added and committed the files to Git using the `git add .` and `git commit -m ""` commands in the terminal window.
5. Linked the Heroku app as the remote master branch using the following command in the terminal window:

    ```heroku git:remote -a <app-name>```

6. Created a requirements.txt file using the following command in the terminal window:

    ```pip3 freeze --local > requirements.txt```

7. Created a Procfile using the following command in the terminal window:

    ```echo web: python <fileName.py> > Procfile```

8. Ran the `git push heroku master` command in the terminal window to push the app to Heroku.
9. Ran the `heroku: ps:scale web=1` command in the terminal window to run the app in Heroku.
10. Entered the following Config Var in Heroku:

    ```MONGO_URI : <link to MongoDB>```


The app was successfully deployed to Heroku at this stage.

### Live App Link

Click the link below to run my project in the live environment:

[Book Shelf]

### Repository Link

Click the link below to visit my project's GitHub repository:

[Book Shelf]

### Running Code Locally

To run my code locally, users can download a local copy of my code to their desktop by completing the following steps:

1. Go to [my GitHub repository]
2. Click on 'Clone or download' under the repository name.
3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.
4. Open 'Git Bash' in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, then paste the URL you copied in Step 3:

    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and create your local clone.
8. Create a new Database in MongoDB  
9. Create collections 
9. Navigate to the `.bashrc` terminal and add your MongoDB URI in the following format:

    ```MONGO_URI="insert your mongo uri details here"```

10. In the terminal, run the `pip3 install -r requirements.txt` command to install the requirements.txt file.
11. You should now be able to run the app locally using the `python3 run.py` command.

## Credits


### Content


### Media


### Acknowledgements


### Disclaimer

This project is for educational purposes only.
