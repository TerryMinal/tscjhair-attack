from flask import Flask, render_template, session, flash, redirect, url_for, request
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

def checkIfLogged():
    return session.get("username")
          
@app.route("/")
def home():
    med = {"art", "photography", "digital", "painting", "music"}
    return render_template("home.html", user="me", mediums=med)

@app.route("/register")
def register():
    if checkIfLogged():
        return redirect(url_for("home"))
    return render_template("register.html")

@app.route("/login")
def login():
    if checkIfLogged():
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/auth", methods=["GET","POST"])
def auth():
    if checkIfLogged():
        return redirect(url_for("home"))
    try:
        usernamein = request.form.get('username')
        passwordin = request.form.get('password')
        if usernamein == "USER" and passwordin == "PASS":
            print "got good info from form"
            session["username"] = usernamein
            print "yayy"
            return redirect(url_for("home"))
        else:
            print "not correct user stuff"
            flash("WRONG USER/PASS COMBO")
            return redirect(url_for("login"))
    except:
        print "except block"
        return redirect(url_for("login"))
        
@app.route("/display")
def display():
    imgs = {"https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwihhvaP9azYAhXDUN8KHXHsAlwQjRwIBw&url=https%3A%2F%2Fwww.pinterest.com%2Fexplore%2Fart%2F&psig=AOvVaw2T78Eget5py0Hr0kAc3YBw&ust=1514557661759202", "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjA88-49azYAhUHMt8KHfWVAO4QjRwIBw&url=http%3A%2F%2Fpawprintnews.com%2F2016%2F09%2Fwhy-mrs-hartzler-chose-art%2F&psig=AOvVaw2T78Eget5py0Hr0kAc3YBw&ust=1514557661759202", "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwihsoO_9azYAhUGY98KHQrJAUsQjRwIBw&url=https%3A%2F%2Ffineartamerica.com%2Ffeatured%2Fthe-spectrum-for-happiness-palette-knife-oil-painting-on-canvas-by-leonid-afremov-leonid-afremov.html&psig=AOvVaw2T78Eget5py0Hr0kAc3YBw&ust=1514557661759202", "https://www.google.com/search?tbm=isch&source=hp&biw=1536&bih=734&ei=Vf9EWtrEMe6nggf84pWgDg&q=art&oq=art&gs_l=img.3..35i39k1l2j0l8.5120.5405.0.5517.5.5.0.0.0.0.163.163.0j1.1.0....0...1ac.1.64.img..4.1.163.0...0.lX2H2ucqC5c#imgrc=oIYxulFa5v0nmM:", "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiVxarh9azYAhWkc98KHYnTAA8QjRwIBw&url=https%3A%2F%2Fwww.pinterest.com%2Fexplore%2Fart%2F&psig=AOvVaw2T78Eget5py0Hr0kAc3YBw&ust=1514557661759202"}
    return render_template("display.html", medium="art", images=imgs)

if __name__ == "__main__":
    app.debug = True
    app.run()
