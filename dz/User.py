import sqlite3 as sql
class User:
    def __init__(self, l_name, f_name, cod, open_accounts):
        self.l_name = l_name
        self.f_name = f_name
        self.cod = cod
        self.open_accounts = open_accounts


    def show(self):
        print(f"Имя владельца счета {self.f_name} {self.l_name}, код {self.cod}")


def adding_a_client():
    l_name = input("Введите фамилию клиента ")
    f_name = input("Введите имя клиента ")
    cod = int(input("Введите код клиента "))
    open_account = int(input("Введите дату создания аккаунта клиента  "))


    with sql.connect("bd.bd") as con:
        cur = con.cursor()

        cur.executescript('''
            insert into person(l_name, f_name, cod, open_accounts)
            values(?, ?, ?, ?)''',
        (l_name, f_name, cod, open_account))