from flask import Flask, render_template, flash, redirect, url_for, session, request
from werkzeug.security import generate_password_hash, check_password_hash
from dbForms import *
from db import *
from functools import wraps
import pymongo

                         



app = Flask(__name__)
app.secret_key = "mysecret key"

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:

            return f(*args, **kwargs)
        else:
            flash("Please logged!")
            return redirect(url_for("login"))
    return decorated_function




@app.route('/')
def home():
   return render_template("index.html")


@app.route('/signup', methods = ["GET", "POST"])
def register():
   
   form = UserRegister(request.form)
   
   if request.method == "POST" and form.validate():
       try:

           user_save(form.username.data, form.email.data,form.password.data)
           flash("created your account, please login.", "success")
           return redirect(url_for("login"))

       except  pymongo.errors.DuplicateKeyError:
           flash( "User already exists!Please choose another username!", "danger" )  
           return redirect(url_for("register")) 
   else:     
       return render_template("signup.html",form=form)


@app.route('/login',methods=["GET","POST"])
def login():
    
    form = LoginUser(request.form)
    if request.method=="POST":
        username = form.username.data
        user = user_collection.find_one({"_id":username })        
        if user and check_password_hash(user['password'], form.password.data):
            flash("Logged in successfully", "success")
            
            session['logged_in'] = True
            session["username"]= username
            return redirect(url_for("dashboard"),username)         
        else:
            flash("Incorrect username or password.", "danger")
            return redirect(url_for("login"))                        
        
    return render_template("login.html",form=form)

@app.route('/logout')
@login_required
def logout():
   session.clear()
   return redirect(url_for("home"))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")

 
if __name__ == "__main__":
    app.run(debug= True)  


    
