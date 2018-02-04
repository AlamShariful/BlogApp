from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

# Set the route and accepted methods
@mod_auth.route('/signin/')
def signin():
    #return "From controller"
    return render_template("auth/signin.html")
