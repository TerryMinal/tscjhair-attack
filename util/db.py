import sqlite3
from hashlib import sha1
#Databases:
    #images: name|id|url|tags
    #users: username|email|password|ml

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
    db = sqlite3.connect(f)
    c = db.cursor()
    inp = "SELECT id FROM " + table + ";"
    r = c.execute(inp)
    new = -1
    for num in r:
        new = num
    print new
    ret =new[0]+1
    return ret


def add_person(username, email, password, ml):
    tempp = sha1(password).hexdigest()
    comm = "INSERT INTO users VALUES (\"" + str(get_table_size('users')) + "\", \"" + username + "\", \"" + email + "\", \"" + tempp + "\", \"" + ml + "\");"
    command(comm)

def add_user(username, password):
    add_person(username, '', password, '{}')

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


print_all_from_table('users')
