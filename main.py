import sqlite3 as sql

with sql.connect("bd1.sql") as con:
    cur = con.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS players(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username nvarchar(10) not null,
            best_score int(6) NOT NULL);

        CREATE TABLE IF NOT EXISTS games(
            username nvarchar(10) not null,
            score int(6) not null,
            id_player INTEGER NOT NULL,
            FOREIGN KEY (id_player) REFERENCES players(id));
        """)
    cur.executescript("""
            INSERT INTO players (username, best_score) VALUES 
                ("Миша",200),
                ("Ваня",154),
                ("Дима",178),
                ("Коля",210);
                
            INSERT INTO games (username, score, id_player) VALUES 
                ("Миша",110,1),
                ("Миша",200,1),
                ("Дима",178,3),
                ("Коля",10,4),
                ("Коля",30,4),
                ("Коля",40,4),
                ("Ваня",154,2),
                ("Коля",210,4); 
        """)
    cur.executescript('''
    select username, count(id_player) from games where username = "Миша"
    ''')
        # 	показать игроков и их кол-во игр по id
    cur.executescript('''
    SELECT username, count(username) FROM games WHERE id_player = 4
    ''')

        # показать игроков и их итоговый счет за все сыгранные игры
    cur.executescript('''
   SELECT username, sum(score) FROM games WHERE id_player = 4
    ''')
        # 	Найти худший результат у каждого игрока
    cur.executescript('''
       SELECT username, min(score) FROM games WHERE id_player = 4
     ''')
