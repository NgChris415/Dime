from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.users_model import Users
from flask_app.models.expenses_model import Expenses
from flask import flash

db = 'Budget'

class Sheets:
    def __init__(self, data):
        self.id = data['id']
        self.monthly_income = data['monthly_income']
        self.savings_goal = data['savings_goal']
        self.month = data['month']
        self.year = data['year']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_sheets(cls):
        query = 'SELECT * FROM sheets JOIN users ON sheets.users_id = users.id;'
        results = connectToMySQL(db).query_db(query)
        return results

    @classmethod
    def get_sheet(cls, data):
        query = "SELECT * FROM sheets WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return cls(results[0])
    
    @classmethod
    def add_sheet(cls, data):
        query = 'INSERT INTO sheets (monthly_income, savings_goal, month, year, users_id) VALUES (%(monthly_income)s, %(savings_goal)s, %(month)s, %(year)s, %(user_id)s);'
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def delete_sheet(cls,data):
        query= 'DELETE FROM sheets WHERE id = %(id)s;'
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update_sheet(cls,form_data):
        query = "UPDATE sheets SET monthly_income = %(monthly_income)s, savings_goal = %(savings_goal)s, month = %(month)s, year = %(year)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,form_data)


    @staticmethod
    def validate_sheet(form_data):
        is_valid = True

        if form_data['monthly_income'] == 0:
            flash("Monthly Income must be greater than 0")
            is_valid = False
        if int(form_data['savings_goal']) <= 0:
            flash("Savings Goal must be greater than 0")
            is_valid = False
        if len(form_data['month']) < 2:
            flash("Month must be greater than 2 characters")
            is_valid = False
        if int(form_data['year']) <= 0:
            flash("Year must be greater than 0")
            is_valid = False
        return is_valid

    @classmethod
    def get_sheet_by_id(cls,data):
        query = 'SELECT * FROM sheets JOIN users ON sheets.users_id = users.id WHERE sheets.id = %(id)s;'
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])
