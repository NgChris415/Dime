from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'Budget'

class Expenses:
    def __init__(self, data):
        self.id = data['id']
        self.sheet_id = data['sheets_id']
        self.location = data['location']
        self.category = data['category']
        self.amount_spent = data['amount_spent']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_expense(cls, data):
        query = "SELECT * FROM expenses WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def add_expense(cls, data):
        query = 'INSERT INTO expenses (location, category, amount_spent, sheets_id) VALUES (%(location)s, %(category)s, %(amount_spent)s, %(sheet_id)s);'
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def delete_sheet(cls,data):
        query= 'DELETE FROM expenses WHERE id = %(id)s;'
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def update_sheet(cls,form_data):
        query = "UPDATE expenses SET location = %(location)s, category = %(category)s, amount_spent = %(amount_spent)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,form_data)

    @staticmethod
    def validate_expense(form_data):
        is_valid = True

        if len(form_data['location']) < 2:
            flash("Location must be at least 2 characters long")
            is_valid = False
        if form_data['amount_spent']== 0:
            flash("Amount Spent must be greater than $0")
            is_valid = False
        return is_valid