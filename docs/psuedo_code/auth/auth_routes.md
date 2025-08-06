# Psuedo Code for Auth/Routes.py

## Import Dependencies

Import Blueprint, render_template, redirect, url_for, flash, request
Import login_user, logout_user, current_user, login_required from flask_login
Import db from your database module
Import User model
Import RegistrationForm and LoginForm (if using Flask-WTF)
Import bcrypt for password hashing

## Initialize Blueprints

auth = Blueprint("auth", __name__)

## Register Route

@auth.route("/register", methods=["GET", "POST"])
def register():
    If current_user is already authenticated:
        Redirect to dashboard or home

    Create instance of RegistrationForm

    If form is submitted and valid:
        Check if a user with this email already exists in the database
            If yes: flash error, redirect to register

        Hash the form password using bcrypt
        Create new User object
        Add user to the database session
        Commit the session
        Flash success message
        Redirect to login

    Return rendered template with form

## Login Route

@auth.route("/login", methods=["GET", "POST"])
def login():
    If current_user is already authenticated:
        Redirect to dashboard or home

    Create instance of LoginForm

    If form is submitted and valid:
        Query the User model using the email
        If user exists and bcrypt confirms password matches:
            Use login_user() to log in the user
            Flash success message
            Redirect to next page (or dashboard)
        Else:
            Flash invalid credentials error

    Return rendered template with form

## Logout Route

@auth.route("/logout")
@login_required
def logout():
    Use logout_user() to clear session
    Flash success message
    Redirect to login or home page

## Protected Route Example

@auth.route("/dashboard")
@login_required
def dashboard():
    Render the dashboard or protected page for the logged-in user

---

## Miscellaneous 

* Register the blueprint in create_app()
* Ensure `User` model implements `UserMixin`
* Initialize `LoginManager` and configure `login_view = 'auth.login'`
* Handle `remember=True` if using "Remember Me" checkbox