from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.users_model import Users
from flask_app.models.sheets_model import Sheets
from flask_app.models.expenses_model import Expenses

@app.route('/sheet/new')
def new_sheet():
    return render_template('new_sheet.html')

@app.route('/sheet/add', methods=['POST'])
def add_sheet():
    if 'user_id' not in session:
        return redirect('/')
    if not Sheets.validate_sheet(request.form):
        return redirect('/sheet/new')
    # import pdb; pdb.set_trace()
    data = {
        'user_id': session['user_id'],
        'monthly_income' : request.form['monthly_income'],
        'savings_goal' : request.form['savings_goal'],
        'month' : request.form['month'],
        'year' : request.form['year'],
    }
    sheet_id = Sheets.add_sheet(data)
    session['sheet_id'] = sheet_id
    return redirect('/dashboard')


@app.route('/sheet/edit/<int:id>')
def edit_sheet_page(id):
    return render_template('edit_sheet.html', sheet=Sheets.get_sheet_by_id({'id':id}))

@app.route('/sheet/edit/submit/<int:id>', methods=['POST'])
def submit_edits(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Sheets.validate_sheet(request.form):
        return redirect(f'/sheet/edit/{id}')
    data = {
        'id': id,
        'monthly_income' : request.form['monthly_income'],
        'savings_goal' : request.form['savings_goal'],
        'month' : request.form['month'],
        'year' : request.form['year'],
    }
    Sheets.update_sheet(data)
    return redirect('/dashboard')

@app.route('/sheet/delete/<int:id>')
def delete_recipe(id):
    Sheets.delete_sheet({'id':id})
    return redirect('/dashboard')

@app.route('/sheet/view/<int:id>')
def view_sheet_page(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template('display_sheet.html', user = Users.get_user(data), sheet=Sheets.get_sheet_by_id({'id':id}))

