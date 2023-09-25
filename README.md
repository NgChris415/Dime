# Production README

Welcome to Dime, a dynamic budget tracking application enabling users to effectively manage finances and achieve savings goals Please check it out [here](insert website here)!
# Table of Contents
1. [Technologies](#technologies)
2. [Features](#features)
3. [Technical Implementations](#technical-implementations)
4. [Future Features](#future-features)

# Technologies

### Frontend
+ ```HTML``` 
+ ```CSS``` 
+ ```Jinja``` 
### Backend
+ ```Flask``` 
+ ```Python```
+ ```MySQL``` 
+ ```Bcrypt``` 

# Features
1. Account creation and log in
2. Creating/deleting budget sheets 
3. Adding/deleting items on budget sheets and allocating them to categories
4. Goal setting and automatic calculation on items added to each budget sheet

### Account Creation/Log In

Users have the capability to establish accounts using the ```Bcrypt``` framework to securely hash their passwords. The website does not store passwords in their original form; instead, it retains password digests and employs built-in Bcrypt methods to validate user credentials. These hashed passwords and emails are stored within a MySQL database, facilitating user login following the account creation process.

<img width="600px" height="400px" alt="dimeloginpage" src="https://github.com/NgChris415/Dime/assets/132420552/28fda545-21e1-448a-95f0-8f5aff215f14">

### Dashboard
The Dashboard displays all the current sheets created, once a sheet is created you are able to add expense, edit, and delete sheet as needed

<img width="600px" height="400px" alt="dimedashboard" src="https://github.com/NgChris415/Dime/assets/132420552/9e52f426-4e0b-4cff-a3d6-dbf635bb504a">


### Create Sheet

Users are able to fill out a form to create sheet for each month/year, each budget sheet is stored in the MySQL database

<img width="600px" height="400px" alt="dimecreatesheet" src="https://github.com/NgChris415/Dime/assets/132420552/4ad4e75e-def3-4018-86dd-c49db92cf72d">


### Add Expense/View Sheet

Users are also able to add expenses to each sheet, as you add expenses you are able to see the remaining money for each month automatically calculated. These values are stored in the MySQL database with a relationship to each individual sheet.

<img width="600px" height="400px" alt="dimeaddexpense" src="https://github.com/NgChris415/Dime/assets/132420552/fff146ed-082f-4dd6-92d0-e672bfcfe276">
<img width="600px" height="400px" alt="dimeviewsheet" src="https://github.com/NgChris415/Dime/assets/132420552/787295ad-d3bd-4013-99ea-bca9edc172d0">




# Technical Implementations

#### Calculations towards goals:
This is the code used in order to use values stored in database to display on the page calculations for each sheet and whether goals are met
```Python
                <p>Monthly Income: {{sheet.monthly_income}}</p>
            </div>
            <div>
                <p>Savings Goal: {{sheet.savings_goal}}</p>
            </div>
            <div>
                <p>Total Spent: {{total_amount_spent}}</p>
                {% set total_remaining = (sheet.monthly_income | int) - total_amount_spent %}
                <p>Total remaining: {{total_remaining}}</p>
            </div>
```


#### Validations
This is an example of one of the Validations used in the app, there are also validations for creating and editing sheets/expenses.
```Python
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
```

# Future Features

In the future I'd like to add:
+ Updating UI by implementing background and using Bootstrap
+ On dashboard, seperate sheets by years for individuals who created multiple sheets
+ Updating forms to allow date/year picker

