import sqlite3
con = sqlite3.connect("databieses.db")
cur = con.cursor()
#CREATE TABLE tsst(title TEXT, genra TEXT, year INTEGER)  #انشاء جدول
mocis = [
    ("the good vader","clen",1975),
    ("the soon","akshan",2050),
    ("the mood","jocke",2001)
]
#cur.executemany('INSERT INTO tsst VALUES(?,?,?)',mocis)
data = cur.execute("SELECT rowid,* from tsst")
print(cur.fetchall())
con.commit()
con.close()