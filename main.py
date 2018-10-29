from flask import Flask, request, redirect, render_template
import cgi, re

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods=['POST'])
def validate_info():
    email_regex = '^(\w+(@){1}\w+(\.){1}\w+)$'
    input_regex = '^\S{3,20}$'

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verification_error = ''
    email_error = ''
    
    if not username or not re.match(input_regex, username) or len(username) < 3 or len(username) > 20:
        username_error = "Not a valid username"
    if not password or not re.match(input_regex, password) or len(password) < 3 or len(password) > 20:
        password_error = "Not a valid password"
    if not verify or verify != password:
        verification_error = "Passwords do not match"
    if email:
        if not re.match(email_regex, email) or len(email) < 3 or len(email) > 20:
            email_error = 'Not a valid email'

        

    if not username_error and not password_error and not verification_error and not email_error:
        return render_template('success.html', title="Welcome!", name=username)
    else:
        return render_template('main.html', title="User Signup", 
        username=username, username_error=username_error,
        password = '', password_error = password_error,
        verification_error = verification_error, verify = '',
        email = email, email_error = email_error)


@app.route("/")
def index():
    return render_template('main.html', title="User Signup")

app.run()