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
    if len(prev_val) == 0:
        next_val = 0
    else:
        next_val = prev_val[0][0] + 1
    c.execute("INSERT INTO ml VALUES('%s', '%d')" %(name, next_val))
        
    db.commit()
    db.close()
