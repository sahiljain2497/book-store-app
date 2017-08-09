import sqlite3

class Database:
        
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,Title TEXT,Author TEXT,Year INTEGER,ISBN INTEGER )")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        self.conn.commit()
        return rows

    def search(self,title='',author='',year='',isbn=''):
        self.cur.execute("SELECT * FROM book WHERE Title=? OR Author=? OR Year=? OR ISBN=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        self.conn.commit()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.conn.commit()
        
    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET Title=? , Author=? , Year=? , ISBN=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()
    #insert('science','einstein','1997','312531')
    #print(view())