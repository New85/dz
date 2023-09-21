import sqlite3
with sqlite3.connect('bd1.sql') as con:
    cur = con.cursor()
    cur.execute('''
                create table if not exists computer(
                    type_pc varchar(20) not null,
                    brand_pc varchar(20) not null,
                    price_pc int(6)
                );
    ''')
    cur.execute('''
    insert into computer(type_pc, brand_pc, price_pc) values
        ('monoblock', 'asus', 49000),
        ('stationary', 'hp', 37800),
        ('laptop', 'Xiaomi', 79500),
        ('laptop', 'hp', 51000),
        ('stationary', 'asus', 49500),
        ('monoblock', 'lenovo', 69000);
    
    ''')

    res = cur.execute('''
                        select type_pc, brand_pc from computer where price_pc > 50000;
    ''')
