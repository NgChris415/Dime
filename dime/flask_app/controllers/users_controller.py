from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.users_model import Users
from flask_app.models.sheets_model import Sheets
from flask_app.models.expenses_model import Expenses
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template('login_page.html')

@app.route('/register', methods=['POST'])
def register():
    if not Users.validate_user(request.form):
        return redirect('/')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : hashed_pw
    }
    user_id = Users.create_user(data)
    session['user_id'] = user_id
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    data = {
        'email' : request.form['email'],
        'password' :request.form['password']
    }
    existing_user = Users.get_user_by_email(data)
    if not existing_user: 
        flash('Invalid email/password')
        return redirect('/')
    if not bcrypt.check_password_hash(existing_user.password, request.form['password']):
        flash('Invalid email/password')
        return redirect('/')
    session['user_id'] = existing_user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template('dashboard.html', user = Users.get_user(data), sheets=Sheets.get_all_sheets())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')