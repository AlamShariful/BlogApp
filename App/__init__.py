from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'blogapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)




@app.route("/")
@app.route("/home/")
def home():
    pageName = "Home"
    return render_template('home.html',pageName=pageName)

from app.mod_auth.controllers import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)


@app.route("/about/")
def about():
    pageName="About"
    return render_template('about.html',pageName=pageName)

@app.route("/blog/")
def blog():
    pageName = "Blog"
    return  render_template('blog.html',pageName=pageName)

@app.route("/login/",methods=['GET', 'POST'])
def login():
    pageName = "Login"
    if request.method == 'POST':
        username = request.form['username']
        passwordfromuser = request.form['password']



        cur = mysql.connection.cursor()
        userexists = cur.execute("SELECT * from users where username=%s", [username])

        if userexists > 0:
            data = cur.fetchone()
            password = data['password']
            #Match Password
            if sha256_crypt.verify(passwordfromuser, password):
                session['logged_in'] = True
                session['username'] = username
                flash("Login Successful","success")
                return redirect(url_for('home'))
            else:
                error = "User Name and Passwoed dosen't Match"
                render_template('login.html', error=error)
            cur.close()

        else:
            error ="User Name Not Found"
            render_template("login.html", error=error)

    return render_template('login.html', pageName=pageName)
    #return "From template"


# Registration Form Class for User registration
class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

#User Registration Controller
@app.route("/registration/",methods=['GET', 'POST'])
def registration():
    pageName = "Registration"
    #error="Err"
    form = RegistrationForm(request.form)
    if request.method =="POST" and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #Create MySql Connection
        cur= mysql.connection.cursor()

        #Insert Query
        cur.execute("INSERT INTO users(name, email, username,password) VALUES(%s,%s,%s,%s)", (name, email, username, password))

        #COmmit to DB
        mysql.connection.commit()

        #Close Connection
        cur.close()

        flash('User Registration Succefull','success')
        #session['username'] = username
        return redirect(url_for('home'))
    return render_template('registration.html', form=form, pageName=pageName)

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('home'))
    return wrap




@app.route("/logout/")
@is_logged_in
def logout():
    session.clear()
    flash('Logout Successfully', 'success')
    return redirect(url_for('login'))
    #return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)

    #app.run()
