import sqlite3
from random import random

def init_db(f='util/ml_db.db'):
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute("CREATE TABLE genre(genre TEXT PRIMARY KEY, val INTEGER)")
    c.execute("CREATE TABLE artist(artist TEXT PRIMARY KEY, val INTEGER)")
    c.execute("CREATE TABLE img(img TEXT PRIMARY KEY, val INTEGER)")
    db.commit()
    db.close()

def add_to_table(content, thing, f='util/ml_db.db'):
    db=sqlite3.connect(f)
    c=db.cursor()
    c.execute("SELECT val FROM %s WHERE val = (SELECT MAX(val) FROM %s)" %(content, content))
    prev_val = c.fetchall()
    # print prev_val
    if len(prev_val) == 0:
        next_val = 0
    else:
        next_val = prev_val[0][0] + 1
    c.execute("INSERT INTO %s VALUES('%s', '%d')" %(content, thing, next_val))
    db.commit()
    db.close()

# finds the word inside the db
# if it exists, it'll return its value
# else return -1
def find_word(content, thing, f='util/ml_db.db'):
    db = sqlite3.connect(f)
    c=db.cursor()
    c.execute("SELECT %s, val FROM %s WHERE %s = '%s' " %(content, content, content, thing))
    val = c.fetchall()
    db.commit()
    db.close()
    if len(val) == 0:
        return -1
    else:
        return val[0][1]

def random_val(content, f='util/ml_db.db'):
    db = sqlite3.connect(f)
    c=db.cursor()
    c.execute("SELECT val FROM %s WHERE val = (SELECT MAX(val) FROM %s)" %(content, content)) # used to get the max val
    max_val = c.fetchall()
    if len(max_val) == 0: #in the case where there is nothing in the table
        return -1
    # print "max: ", max_val[0][0] + 1
    i = random() * (max_val[0][0] + 1)
    c.execute("SELECT %s, val FROM %s WHERE val = '%d' " %(content, content, i)) # gets a random name and value pair
    val = c.fetchall()
    # print val
    db.commit()
    db.close()
    return [int(val[0][1]), val[0][0]]


# init_db('ml_db.db')
# add_to_table("img", "pie", "./ml_db.db")
# add_to_table("img", "happy", "./ml_db.db")
# add_to_table("img", "pew", "./ml_db.db")
# add_to_table("img", "sad", "./ml_db.db")
# print find_word("genre", "cool", './ml_db.db')
# print find_word("genre", "pew", './ml_db.db')
# print random_val("genre", './ml_db.db')
# print random_val("genre")
