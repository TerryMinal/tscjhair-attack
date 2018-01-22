from flask import Flask, render_template, session, flash, redirect, url_for, request
import os
import json
import time
from util import db, ml_db, ml
from util import apicalling as api

app = Flask(__name__)
app.secret_key = os.urandom(32)

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
    med = {"art", "music"}
    if checkIfLogged():
        try:
            parameters = [int(i) for i in (db.get_ml_by_id(session["username"]).split(',')) ]
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
            try:
                db.add_user(req['username'], req['password0'])
                session["username"]=req["username"]
                return redirect(url_for("home"))
            except:
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
    try:
        usernamein = request.form.get('username')
        passwordin = request.form.get('password')
        if db.get_authentication(usernamein, passwordin): #usernamein == "USER" and passwordin == "PASS":
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
    # imgs=[getty() for i in range(5) ]
    # use same function that gets 3 random and 2 predicted
    if checkIfLogged():
        return render_template("display.html", medium="art", images=imgs)
    return redirect(url_for("home"))

@app.route("/update_display")
def update_display():
    data=request.args.get("replace_pics")
    # arr is a json of data abot song/art
    # convert arr to an array mapping strings to numbers based on ml_db
    # update training set
    # optimize parameters
    # using parameters (genre, artist) pass into the predict function
    # finds random genres in ml_db and pass it into the predict function
    # if the predict function retursn > .5, send it to the user
    # get imgs/music from the ml_db (maybe have to separate ml_db into music and imgs)
    # return 3 random and 2 predicted images
    ml.append_train_set(arr, tsetX, tsetY)
    parameters = ml.optimize(parameters, tsetX, tsetY)
    # predict(parameters, x) # x is a list of data retrieved from ml_db
    # img = apicalling.getty()
    # new_data = apicalling.clarifai
    response={'new_pics': data}
    #response=(calls getty)
    return json.dumps(response)

@app.route("/logout")
def logout():
    session.pop("username")
    return redirect(url_for("home"))

# @app.route('/spotify') #Just for testing
# def spotify():
#     return render_template('spotify.html')

def get_content(thing):
    result = []
    count = 0
    # if (thing == "music"):
    #     genre = [ml_db.random_val("genre") for i in range(7)]
    #     artist [ml_db.random_val("artist") for i in range(7)]
    #     count = 0
    #     for music in genre:
    #         for singer in artist:
    #             if (predict(parameters, [music, singer]) >= .5):
    #                 count++
    #                 result.append()
    if (thing == "art"):
        img = [ [ml_db.random_val("img") for i in range(len(parameters))] for i in range(10) ]
        for i in range(10):
            if (ml.predict(parameters, img[i]) >= .5):
                result.append(img[i])
                count += 1
            if (count >= 2):
                break
    data = []
    for i in range(5 - len(result)): #assures that we get 5 images
        t = api.getty(ml_db.random_val("img"))
        data.append([t, api.clarifai(t)])
    for i in range(len(result)):
        t = api.getty(result[i])
        data.append([t, api.clarifai(t)])
    # x = [ml_db.random_val() for i in range(5)] # do this for each db
    # predict(parameters, x) # i think i need to create a db for images, genre, and artists, might as well do
    # features while im at it

if __name__ == "__main__":
    app.debug = True
    app.run()
