from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)
app.config['DEBUG'] = True

def validate_username(username):
    if len(username) >= 3 and len(username) < 20:
        if " " not in username:
            return ''
        else:
            username_error = 'Spaces are not allowed in username'
            username = ''
            return username_error
    else:
        username_error = 'Username must be between 3 and 20 characters long'
        username = ""
        return username_error

def validate_password(password, verify_password):
    if len(password) >= 3 and len(password) <= 20:
        if " " not in password:
            if password == verify_password:
                return ''
            else:
                password_error = 'Passwords do not match'
                return password_error
        else:
            password_error = 'Spaces are not allowed in password'
            return password_error
    else:
        password_error = 'Password must be between 3 and 20 characters long'
        return password_error

def validate_email(email):
    """Validate the email address using a regex."""
    if not re.match("^[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9.-]+$", email):
        email_error = 'Please enter a valid email'
        return email_error
    else:
        return ''

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', title='User Login')

@app.route("/", methods=['POST'])
def validate_input():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = validate_username(username)
    password_error = validate_password(password, verify_password)
    email_error = validate_email(email)

    if not username_error and not password_error and not email_error:
        return render_template('welcome.html', username=username)

    else:
        return render_template('index.html', title='Welcome', username=username, email=email,
        username_error=username_error,
        email_error=email_error,
        password_error=password_error)

app.run()
