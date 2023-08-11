from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


db = 'Budget'

class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        print('##########################################')
        return cls(results[0])

    @classmethod
    def create_user(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);'
        results = connectToMySQL(db).query_db(query, data)
        return results

    @staticmethod
    def validate_user(form_data):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, form_data)
        if len(form_data['first_name']) < 2:
            flash('First Name must be at least 3 characters')
            is_valid = False
        if len(form_data['last_name']) < 2:
            flash('Last Name must be at least 3 characters')
            is_valid = False
        if len(results) >= 1:
            flash('Email is already taken')
            is_valid = False
        if not EMAIL_REGEX.match(form_data['email']):
            flash('Invalid Email Address')
            is_valid = False
        if form_data['password'] != form_data ['confirm_password']:
            flash("Passwords do not match")
            is_valid = False
        if len(form_data['password']) < 8:
            flash('Password must be at least 8 characters long')
            is_valid = False
        return is_valid
    
    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])