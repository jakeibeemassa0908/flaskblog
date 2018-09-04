from flask import render_template,url_for,flash,redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm,LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author':'Jacques Massa',
        'title':'Blog post 1',
        'content':'First post',
        'date_posted':'September 1st 2018'
    },
    {
        'author':'Ann-Marie',
        'title':'Blog post 2',
        'content':'Second post',
        'date_posted':'September 1st 2018'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.htm',posts = posts)

@app.route("/about")
def about():
    return render_template("about.htm",title='About')

@app.route("/register",methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('registration.htm',title = "Register",form=form)

@app.route("/login",methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'jimassa@uh.edu' and form.password.data == 'password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.htm',title = "Login",form=form)