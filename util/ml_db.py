import sqlite3

def init_db(f='util/ml_db.db'):
    db = sqlite3.connect(f)
    c = db.cursor()
    c.execute("CREATE TABLE ml(name TEXT PRIMARY KEY, val INTEGER)")
    db.commit()
    db.close()

def add_to_table(name, f='util/ml_db.db'):
    db=sqlite3.connect(f)
    c=db.cursor()
    c.execute("SELECT val FROM ml WHERE val = (SELECT MAX(val) FROM ml)")
    prev_val = c.fetchall()
    print prev_val
    if len(prev_val) == 0:
        next_val = 0
    else:
        next_val = prev_val[0][0] + 1
    c.execute("INSERT INTO ml VALUES('%s', '%d')" %(name, next_val))

    db.commit()
    db.close()

# finds the word inside the db
# if it exists, it'll return its value
# else return -1
def find_word(name, f='util/ml_db.db'):
    db = sqlite3.connect(f)
    c=db.cursor()
    c.execute("SELECT name, val FROM ml WHERE name = '%s' " %name)
    val = c.fetchall()
    db.commit()
    db.close()
    if len(val) == 0:
        return -1
    else:
        return val[0][1]


# init_db('ml_db.db')
# add_to_table("pew", "./ml_db.db")
print find_word("cool", './ml_db.db')
print find_word("dne", './ml_db.db')
