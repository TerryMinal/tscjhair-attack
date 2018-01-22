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

print get_ml('shaina')
