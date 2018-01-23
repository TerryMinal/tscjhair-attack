import sqlite3
from hashlib import sha1
from random import random
#Databases:
    #images: name|id|url|tags
    #users: username|email|password|ml

#try init_db()
#f='util/data.db'
#check for valid username passwords

def init_db(f='util/data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute("CREATE TABLE images(name TEXT PRIMARY KEY, id INTEGER, url TEXT, tags TEXT)")
    c.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT, password TEXT, ml TEXT)")
    db.commit()
    db.close()


def command(command, f='util/data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()
    r = c.execute(command)
    db.commit()
    db.close()
    return r

def return_command(command, f='util/data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()
    r = c.execute(command)
    return r

def print_all_from_table(table, f='util/data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()
    inp = "SELECT * FROM " + table + ";"
    r = c.execute(inp)
    for entry in r:
        print entry

def get_table_size(table, f='util/data.db'):
    #inefficent but fight me
    db=sqlite3.connect(f)
    c=db.cursor()
    c.execute("SELECT id FROM %s WHERE id = (SELECT MAX(id) FROM %s)" %(table, table))
    prev_val = c.fetchall()
    # print prev_val
    if len(prev_val) == 0:
        next_val = 0
    else:
        next_val = prev_val[0][0] + 1
    return next_val

def get_ml(username):
    comm = "SELECT ml FROM users WHERE username=\"" + username + "\""
    db = sqlite3.connect('util/data.db')
    c = db.cursor()
    mlget = c.execute(comm)
    for ml in mlget:
        return ml[0]
    db.commit()
    db.close()

def alter_ml(username, new_ml):
    comm = "UPDATE users SET ml = ? WHERE username = ?"
    db = sqlite3.connect('util/data.db')
    c = db.cursor()
    params = (new_ml, username)
    c.execute(comm, params)
    db.commit()
    db.close()

#print get_ml('shaina')
def add_person(username, email, password, ml):
    tempp = sha1(password).hexdigest()
    comm = "INSERT INTO users VALUES (\"" + str(get_table_size('users')) + "\", \"" + username + "\", \"" + email + "\", \"" + tempp + "\", \"" + ml + "\");"
    command(comm)

def add_user(username, password, f="util/data.db"):
    db=sqlite3.connect(f)
    c=db.cursor()
    c.execute("SELECT * FROM users WHERE username = \"" + username + "\"")
    prev_val = c.fetchall()
    # print prev_val
    if len(prev_val) == 0:
        add_person(username, '', password, '{}')
        return True
    else:
        return False
    
def get_ml_by_id(id, f='util/data.db'):
    db = sqlite3.connect(f)
    c = db.cursor()
    inp = "SELECT ml FROM users WHERE id=\"" + str(id) + "\";"
    r = c.execute(inp)
    tup = None
    for entry in r:
        tup = entry[0]
    return tup

def edit_ml_by_id(id, ml, f='util/data.db'):
    comm = "UPDATE users SET ml=\"" + ml + "\" WHERE id=\""+str(id)+"\";"
    command(comm)

def get_authentication(username, password, f='util/data.db'):
    comm = "SELECT * FROM users WHERE username=\""+username+"\";"
    user = return_command(comm)
    for use in user:
        if use[3] == sha1(password).hexdigest():
            return True
    return False
        #for us in use:
        #    print us
    #if password==use

def load_image_to_db(name, id, url, tag):
    comm = "INSERT INTO images VALUES (\"" + name + "\", \"" + id + "\", \"" + url + "\", \""+ tag +"\")"
    command(comm)

def get_5_images():
    fetch_image = return_command("SELECT * FROM images")
    images = []
    for image in fetch_image:
        images.append(image)
    return_images = []
    for i in range(5):
        r = -1
        while r == -1 or r in return_images:
            r = (int)( random() * len(images))
        return_images.append(r)
    ret = []
    for ri in return_images:
        ret.append(images[ri])
    return ret
