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




@app.route("/")
@app.route("/home/")
def home():
    pageName = "Home"
    cur = mysql.connection.cursor()
    allposts = cur.execute("SELECT * from posts WHERE approved=%s ORDER BY id DESC",['yes'])
    articles = cur.fetchall()
    cur.close()

    if allposts > 0:
        return render_template('home.html', pageName=pageName, articles=articles)
    else:
        msg = "No Post Found"
        return render_template('home.html', pageName=pageName, msg=msg)
    #return render_template('home.html',pageName=pageName)

from app.mod_auth.controllers import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)
# app.register_blueprint(xyz_module)

@app.route('/dashboard/')
@is_logged_in
def dashboard():
    pageName="Dashboard"
    if session['username']=='admin':
        cur = mysql.connection.cursor()
        allposts = cur.execute("SELECT * from posts ORDER BY id DESC")
        articles = cur.fetchall()
        #cur.close()

        if allposts > 0:
            return render_template('dashboard.html', pageName=pageName, articles=articles)
        else:
            msg = "No Post Found"
            return render_template('dashboard.html', pageName=pageName, msg=msg)
    else:
        cur = mysql.connection.cursor()
        allposts = cur.execute("SELECT * from posts WHERE user_id=%s ORDER BY id DESC",[session['userid']])
        articles = cur.fetchall()
        #cur.close()

        if allposts > 0:
            return render_template('dashboard.html', pageName=pageName, articles=articles)
        else:
            msg = "No Post Found"
            return render_template('dashboard.html', pageName=pageName, msg=msg)


@app.route('/dashboard/edit/<string:id>/',methods=['GET', 'POST'])
@is_logged_in
def edit(id):
    pageName="Edit Post"
    cur = mysql.connection.cursor()

    ##### After User Edit the Post then Submit For DataBase Update
    if request.method == "POST":
        title = request.form['title']
        postbody = request.form['postbody']

        # remove the <P> and </P> tag
        postbody = postbody.replace('<p>', '').replace('</p>', '')

        cur = mysql.connection.cursor()

        # Execute
        cur.execute("UPDATE posts SET title=%s, body=%s, approved=%s WHERE id=%s ",(title, postbody,'waiting',id))
        # Commit to DB
        mysql.connection.commit()
        # Close connection
        cur.close()

        flash('Post Submit for approval', 'success')
        return redirect(url_for('dashboard'))

    ### Load the Data into edit Form for View
    ## First check if the user is the owner of this post
    editposts = cur.execute("SELECT * from posts WHERE id=%s", [id])
    data = cur.fetchone()
    user_id= data['user_id']
    if session['userid']!= user_id:
        flash('You are Not authorised to Edit this Post', 'danger')
        return redirect(url_for('dashboard'))

    if editposts > 0:
        return render_template('editpost.html', pageName=pageName, data=data)
    else:
        msg = "No Post Found"
        return render_template('dashboard.html', pageName=pageName, msg=msg)


@app.route('/dashboard/delete/<string:id>/')
@is_logged_in
def delete(id):
    cur = mysql.connection.cursor()
    ## First check if the user is the owner of this post
    cur.execute("SELECT * from posts WHERE id=%s", [id])
    data = cur.fetchone()
    user_id = data['user_id']
    if session['userid'] != user_id:
        flash('You are Not authorised to Delete this Post', 'danger')
        return redirect(url_for('dashboard'))
    # Get article
    result = cur.execute("DELETE FROM posts WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    if result > 0:
        flash("Post has been Deleted", 'success')
        return redirect(url_for('dashboard'))
    else:
        error = "Some This went Wrong, Please try again Later"
        return redirect(url_for('dashboard', error=error))


@app.route('/dashboard/postdisapprove/<string:id>/')
@is_logged_in
def postdisapprove(id):
    cur = mysql.connection.cursor()

    # check if the user is the Admin
    if session['username'] != 'admin':
        flash('You are Not authorised to Disapproved Post', 'danger')
        return redirect(url_for('dashboard'))
    # Get article
    result = cur.execute("UPDATE posts SET approved=%s WHERE id = %s", ('waiting', id))
    mysql.connection.commit()
    cur.close()
    if result > 0:
        flash("Post has been Disapproved", 'success')
        return redirect(url_for('dashboard'))
    else:
        error = "Some This went Wrong, Please try again Later"
        return redirect(url_for('dashboard', error=error))



@app.route('/dashboard/postapprove/<string:id>/')
@is_logged_in
def postapprove(id):
    cur = mysql.connection.cursor()
    # check if the user is the Admin
    if session['username'] != 'admin':
        flash('You are Not authorised to Approve Post', 'danger')
        return redirect(url_for('dashboard'))

    # Get article
    result = cur.execute("UPDATE posts SET approved=%s WHERE id = %s",('yes',id))
    mysql.connection.commit()
    cur.close()
    if result>0:
        flash("Post Approved",'success')
        return redirect(url_for('dashboard'))
    else:
        error="Some This went Wrong, Please try again Later"
        return redirect(url_for('dashboard',error=error))

@app.route('/dashboard/newpost/saveas/',methods=['GET', 'POST'])
@is_logged_in
def saveas():
    return "save as"

@app.route("/dashboard/newpost/",methods=['GET', 'POST'])
@is_logged_in
def newpost():
    if request.method=="POST":
        title= request.form['title']
        postbody=request.form['postbody']

        #remove the <P> and </P> tag
        postbody = postbody.replace('<p>', '').replace('</p>', '')

        cur= mysql.connection.cursor()

        # Execute
        cur.execute("INSERT INTO posts(user_id,title, body, author,approved) VALUES(%s, %s, %s, %s, %s)", (session['userid'],title, postbody, session['name'], 'waiting'))

        # Commit to DB
        mysql.connection.commit()
        # Close connection
        cur.close()

        flash('Post Submit for approval', 'success')

        return redirect(url_for('dashboard'))




    return render_template('newpost.html')

@app.route("/about/")
def about():
    pageName="About"
    return render_template('about.html',pageName=pageName)

@app.route("/blog/")
def blog():
    pageName = "Blog"
    return render_template('blog.html',pageName=pageName)

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
            name=data['name']
            userid=data['id']
            #Match Password
            if sha256_crypt.verify(passwordfromuser, password):
                session['logged_in'] = True
                session['username'] = username
                session['name']= name
                session['userid']=userid
                flash("Login Successful","success")
                return redirect(url_for('home'))
            else:
                error = "User Name and Passwoed dosen't Match"
                return render_template('login.html', error=error)
            cur.close()

        else:
            error ="User Name Not Found"
            return render_template("login.html", error=error)

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

        # check for unique username and email
        getusername=cur.execute("SELECT * FROM users WHERE username=%s", [username])
        getemail = cur.execute("SELECT * FROM users WHERE email=%s", [email])
        #userdata=cur.fetchall()

        if getusername > 0:
           error="This User name is already Taken, Please try another one"
           return render_template('registration.html',form=form,error=error,pageName=pageName)
        elif getemail > 0:
            error = "This Email is already registered, Please try another one"
            return render_template('registration.html', form=form, error=error, pageName=pageName)
        else:
            #Insert Query
            cur.execute("INSERT INTO users(name, email, username,password) VALUES(%s,%s,%s,%s)", (name, email, username, password))
            #COmmit to DB
            mysql.connection.commit()
            #Close Connection
            cur.close()

            flash('User Registration Succefull','success')
            #session['username'] = username
            return redirect(url_for('login'))

    return render_template('registration.html', form=form, pageName=pageName)

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
