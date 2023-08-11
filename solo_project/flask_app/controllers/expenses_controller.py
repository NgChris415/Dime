from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.users_model import Users
from flask_app.models.sheets_model import Sheets
from flask_app.models.expenses_model import Expenses

@app.route('/sheet/view/<int:id>/expense/form')
def expense_form(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template ('new_expense.html', user = Users.get_user(data), sheet=Sheets.get_sheet_by_id({'id':id}))

@app.route('/sheet/view/<int:id>/expense/form/submit', methods=['POST'])
def submit_expense(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Expenses.validate_expense(request.form):
        return redirect('/sheet/view/<int:id>/expense/form')
    import pdb; pdb.set_trace()
    data = {
        'sheet_id': id,
        'location' : request.form['location'],
        'category' : request.form['category'],
        'amount_spent' : request.form['amount_spent']
    }
    Expenses.add_expense(data)
    print('################################################')
    return redirect('/dashboard')