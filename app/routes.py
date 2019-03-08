from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from random import randint
import matplotlib.pyplot as plt
import matplotlib

@app.route('/')
@app.route('/index')
@login_required
def index():
    # create image file local to server
    tGraph(current_user.temp_sensors)
    hGraph(current_user.humid_sensors)
    return render_template('index.html', title='Home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        user.set_temp_sensors(form.tempsensors.data)
        user.set_humid_sensors(form.humidsensors.data)
        db.session.add(user)
        db.session.commit()
        flash('Registered!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        #return redirect((url_for(next_page)[0])[1:])
        return redirect('index')  # XXX placeholder!
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# function that generates 24 random temperature
def temperature():
    temperature = [randint(20, 100) for i in range(24)]
    return temperature

# function that generates 24 random humidity
def humidity():
    humidity = [randint(30, 60) for i in range(24)]
    return humidity

# generates temperature graph in local folder
def tGraph(times):
    matplotlib.use('Agg')
    for i in range(times):
        plt.clf()
        time = list(range(24))
        plt.plot(time, temperature(), color="blue")
        plt.xlabel('Time interval / hour')
        plt.ylabel('Temperature / F')
        path = 'app/static/images/tGraph' + current_user.username + `i`
        plt.savefig(path)

# generates humidity graph in local folder
def hGraph(times):
    matplotlib.use('Agg')
    for i in range(times):
        plt.clf()
        time = list(range(24))
        plt.plot(time, humidity(), color="orange")
        plt.xlabel('Time interval / hour')
        plt.ylabel('Humidity / %')
        plt.savefig('app/static/images/hGraph%d.png' % i)
        path = 'app/static/images/hGraph' + current_user.username + `i`
        plt.savefig(path)
