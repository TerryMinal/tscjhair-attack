from flask import Flask, render_template, session, flash, redirect, url_for, request
import os
import json
import time
from util import db

app = Flask(__name__)
app.secret_key = os.urandom(32)

def checkIfLogged():
    return session.get("username")

@app.route("/")
def home():
    med = {"art", "photography", "digital", "painting", "music"}
    if checkIfLogged():
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
        if req['password0'] == req['password1']:
            #NEED TO CHECK IF USERNAME IS ALREADY TAKEN
            db.add_user(req['username'], req['password0'])
            session["username"]=req["username"]
            return redirect(url_for("home"))
        else:
            flash("Register was not successful. Please try again.")
    if checkIfLogged():
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
    try:
        usernamein = request.form.get('username')
        passwordin = request.form.get('password')
        #return db.get_authentication(usernamein, passwordin)
        if db.get_authentication(usernamein, passwordin): #usernamein == "USER" and passwordin == "PASS":
            flash("test")
            session["username"] = usernamein
            return redirect(url_for("home"))
        else:
            flash("Login was not successful. Please try again.")
            return redirect(url_for("login"))
    except:
        return "hi"
        return redirect(url_for("login"))

@app.route("/display")
def display():
    imgs={"https://thumb1.shutterstock.com/display_pic_with_logo/158830/550002070/stock-vector-art-pop-art-illustration-pop-art-design-template-for-art-gallery-art-studio-school-of-the-arts-550002070.jpg", "http://pawprintnews.com/wp-content/uploads/2016/09/Art.jpg", "https://www.saci-florence.edu/sites/default/files/img/promo/maria_nissan_923x563.jpg","http://cdn.shopify.com/s/files/1/0822/1983/articles/baby-pooh-pixel-art-pixel-art-baby-pooh-winnie-the-pooh-pooh-bear-pooh-disney-pixel-8bit.png?v=1501258328", "https://i.pinimg.com/736x/a5/58/6a/a5586acfff0d5ddd5e3fd3b2bf9eda6b--pony-bead-patterns-perler-patterns.jpg"}
    if checkIfLogged():
        return render_template("display.html", medium="art", images=imgs)
    return redirect(url_for("home"))

@app.route("/update_display")
def update_display():
    data=request.args.get("replace_pics")
    print(data)
    response={'new_pics': data}
    #response=(calls getty)
    return json.dumps(response)

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.debug = True
    app.run()
