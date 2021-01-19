from flask import Flask, redirect, render_template, request, session

from datetime import datetime
from pymongo import MongoClient


app = Flask(__name__)

app.secret_key = '12345678'

client = MongoClient(
    'mongodb+srv://minh:123@cluster0.yyfoe.mongodb.net/test?retryWrites=true&w=majority')
db = client.test


@app.route('/home')
def fri():
    return render_template('python.html')


@app.route('/')
def index():
    if 'email' in session:
        return render_template('python.html')
    else:
        return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login_fo():
    if request.method == 'GET':
        return render_template('log.html')
    elif request.method == 'POST':
        login_user = db.users.find_one({'email': request.form['email']})

        if login_user:
            if login_user['password'] == request.form['password']:
                session['email'] = request.form['email']
                return render_template('python.html')
            else:
                return redirect('/login')
        else:
            return redirect('/login')

        # return "Invalid name or password"


@app.route('/register', methods=['GET', 'POST'])
def regis():
    if request.method == 'GET':
        return render_template('regi.html')
    elif request.method == 'POST':
        # form = request.form
        # email = form['email']
        # passwd = form['password']
        new_user = db.users.find_one({'email': request.form['email']})

        if new_user is None:
            db.users.insert_one(
                {'email': request.form['email'], 'password': request.form['password'], 'fullname': request.form['firstname'] + ' ' + request.form['lastname']})
            session['email'] = request.form['email']
            return redirect('/')

        return redirect('/register')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/logout')
def out():
    session.pop('email')
    return redirect('/')


@app.route('/learn')
def learn():
    return render_template('learn.html')


@app.route('/profiles')
def pro():
    if 'email' not in session:
        return redirect('/')


@app.route('/beginner')
def beg():
    return render_template("beginner.html")


@app.route('/inter')
def inter():
    return render_template("inter.html")


@app.route('/advance')
def adv():
    return render_template("advance.html")


@app.route('/contact')
def us():
    return render_template("contact.html")


@app.route('/install')
def install():
    return render_template("install.html")


@app.route('/syntax')
def syn():
    return render_template("syntax.html")


@app.route('/structure')
def stru():
    return render_template("data.html")


@app.route('/algo')
def algo():
    return render_template("algo.html")


if __name__ == '__main__':
    app.run(debug=True)
