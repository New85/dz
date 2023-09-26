import sqlite3 as sq

with sq.connect('testbd.sql') as con:
    cur = con.cursor()
    cur.executescript('''
            create table if not exists people(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sname varchar(10) not null,
            city varchar(10) not null,
            comm int(3) not null);
            
            create table if not exists customers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cname varchar(10) not null,
            city varchar(10) not null,
            rating int(5) not null,
            id_sp integer,
            FOREIGN KEY (id_sp) REFERENCES people(id));
            ''')
Salespeople = []
with open("salespeople.txt","r", -1, 'utf-8') as f:
    for l in f:
        l = l.split()
        l = tuple(l)
        print(l)
        Salespeople.append(l)

print(Salespeople)
Customers = []
with open("customers.txt","r", -1,'utf-8') as m:
    for i in m:
        i = i.split()
        i = tuple(i)
        print(i)
        Customers.append(i)
print(Customers)