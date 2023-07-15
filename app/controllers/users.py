from flask import render_template,redirect,session,request, flash
from app import app
from app.models.user import User
#from app.models.quote import Quote
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['POST'])
def register():
    print (request.form)
    if not User.validate_register(request.form):
        return redirect('/')
    data ={ 
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    print(request.form)
    data = { 'email': request.form['email']}
    user = User.get_by_email(data)

    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = {
        "user_id": user.id
    }
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')

    user_id = session['user_id']['user_id']
    user = User.get_by_id(user_id)

    if not user:
        flash("Invalid User","dashboard")
        return redirect('/logout')

    data = {
        'id': user.id
}

    return render_template('dashboard.html', data=data)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')