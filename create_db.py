import sqlite3
def create_db():
    con=sqlite3.connect(database=r'tbs.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,supdate text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS stock(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier text,itemname text,hsncode text,price text,qty text,discount text)")
    con.commit()


create_db()