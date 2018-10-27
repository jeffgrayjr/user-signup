from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route('/', methods=['POST'])
def validate_info():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
    if username:
        return render_template('success.html', name=username)
    else:
        return render_template('main.html')

@app.route('/successful', methods=["get"])
def successful():
    username = request.args.get('username')
    return '<h1>Welcome, {0}!</h1>'.format(username)

@app.route("/")
def index():
    return render_template('main.html')

app.run()