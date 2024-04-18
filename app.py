# import uuid
from ast import dump
from collections import OrderedDict
from flask import Flask, redirect, render_template, url_for, request
    
app = Flask(__name__)

expenses = OrderedDict({
    'borak' : {
        'id' : 3,
        'expense_detail' : 'sth',
        'category' : 'sth',
        'amount' : 'sth',
        'date' : '2019-02-24'
    },
    'mohak' : {
        'id' : 3,
        'expense_detail' : 'sth',
        'category' : 'sth',
        'amount' : 'sth',
        'date' : '2019-02-24'
    }
})

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('user_form.html')
    else:
        for _, person in admins.items():         
            if(request.form['username'] == person["name"] and request.form['password'] == person["password"]):
                return redirect(url_for('getexpense'))
            
        return "<h4>Sorry but no user exists </h4>"

@app.route('/test/<int:id>')
def test(id : int):
    return f"<p>Something with id : {id} </p>"

@app.get('/getexpense')
def getexpense():
    return render_template('expense_form.html.jinja', expenses=expenses)

@app.post('/getexpense')
def addexpense():
    new_exp = OrderedDict([('id', len(expenses)+1), ('expense_detail', request.form['expense_detail']), ('category', request.form['category']), ('amount', request.form['amount']), ('date', request.form['date'])])
    expenses.update({ request.form['expense_detail'] : new_exp })
    return redirect(url_for('getexpense'))

@app.route('/viewtable')
def viewTable():
    return render_template('table.html')

if __name__ == '__main__':
    app.run(debug=True)
    