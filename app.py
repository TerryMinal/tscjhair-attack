from flask import Flask, render_template, session, flash, redirect, url_for, request
import os
import json
from util.content import get_content
from util import db, ml_db, ml
from util import apicalling as api

app = Flask(__name__)
app.secret_key = os.urandom(32)

api.getKey("credentials.txt")

parameters = []
tsetX = []
tsetY = []

try:
    db.init_db()
except:
    print "db has already been created!"

def checkIfLogged():
    return session.get("username")

@app.route("/")
def home():
    med = {"art"}
    if checkIfLogged():
        try:
            global parameters
            parameters = [int(i) for i in (db.get_ml_by_user(session["username"]).split(',')) ]
            print "parameters:", parameters
        except:
            print "no data in parameter"
        print "logged in"
        return render_template("home.html", user=session["username"], mediums=med)
    else:
        print "notlogged"
        return render_template("login.html", notlogged=True)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #db.add_user(request.form[])
        req = request.form

        if req['username'] == "":
            flash("Please enter a username!")
        elif req['password0'] != req['password1']:
            flash("Passwords do not match!")
        elif req['password0']=='':
            flash("Please enter a password!")
        else:
            if(db.add_user(req['username'], req['password0'])):
                session["username"]=req["username"]
                global parameters
                parameters = db.get_ml_by_user(req["username"])
                return redirect(url_for("home"))
            else:
                flash("Username taken. Please try another one.")
    if checkIfLogged():
        # db.edit_ml_by_id(req['username'], ml.populate_parameters())
        return redirect(url_for("home"))
    return render_template("register.html", notlogged=True)

@app.route("/login")
def login():
    if checkIfLogged():
        return redirect(url_for("home"))
    return render_template("login.html", notlogged=True)

@app.route("/auth", methods=["GET","POST"])
def auth():
    if checkIfLogged():
        return redirect(url_for("home"))
    #try:
    usernamein = request.form.get('username')
    passwordin = request.form.get('password')
    if db.get_authentication(usernamein, passwordin): #usernamein == "USER" and passwordin == "PASS":
        session["username"] = usernamein
        global parameters
        parameters = db.get_ml_by_user(usernamein)
        print parameters
        parameters = json.loads(parameters)
        return redirect(url_for("home"))
    else:
        flash("Login was not successful. Please try again.")
        return redirect(url_for("login"))
    #except:
    #    return "hi"
    #return redirect(url_for("login"))

@app.route("/display")
def display():
    if checkIfLogged():
        global parameters
        imgs= get_content(parameters, "img")
        print len(imgs)
        imgs=json.loads(imgs)
        return render_template("display.html", medium="art", images=imgs)
    else:
        return redirect(url_for("home"))

@app.route("/update_display")
def update_display():
    global parameters
    data = request.args.get("replace_pics")
    data = json.loads(data)
    print "\n\n\n\n\n\n\n\n"
    print data
    print "\n\n\n\n\n\n\n\n"
    for i in data:
        print i
    c = [ [int(ml_db.get_word_num("img", x)) for x in api.clarifai(i)] for i in data]
    d = []
    for x in c:
        d.append(x[:3]) #takes only the first three parameters
    # update training set
    # optimize parameters
    # return 3 random and 2 predicted images
        #print "\n========================x: \n", x
    print "\n\n\n\n\n\n\n\n"
    print "d: ", d
    print "\n\n\n\n\n\n\n\n end of d"
    global tsetX
    global tsetY
    for i in d:
        ml.append_train_set(i, tsetX, tsetY)
    parameters = ml.optimize_parameters(parameters, tsetX, tsetY)
    #print parameters
    print "\n\n\n\n\n\n\n\n"
    print "parameters: ", parameters 
    print "\n\n\n\n\n\n\n\n"
    #predict(parameters, x) # x is a list of data retrieved from ml_db
    img = get_content(parameters, "img")
    print "\n\n\n\n\n\n\n\n"
    print img
    print "\n\n\n\n\n\n\n\n"
    # response = json.loads(img)
    #response=(calls getty)
    #img = json.dumps(img)
    return img

@app.route("/logout")
def logout():
    db.edit_ml_by_user(session["username"], json.dumps(parameters))
    session.pop("username")
    return redirect(url_for("home"))

# @app.route('/spotify') #Just for testing

# def spotify():
#     return render_template('spotify.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
