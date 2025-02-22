import sqlite3

from infra.db import get_db

# Conecte-se ao banco de dados
conn,cursor = get_db()


# Liste as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())


user = 123
cursor.execute(f"SELECT * FROM user;")
print(cursor.fetchall())
# cursor.execute("DROP TABLE personagens;")
# print(cursor.fetchall())
cursor.execute("PRAGMA table_info(user);")
print(cursor.fetchall())

# classes = ['Guerreiro', 'Mago', 'Arqueiro', 'Assassino']
# for classe in classes:
#     cursor.execute(f"""SELECT * FROM classes WHERE classe = '{classe}';""")
#     resultado = cursor.fetchone()
#     print(classe)
#     if not resultado:
#         cursor.execute(f"""INSERT INTO classes (classe,base_dmg,base_hp,percent_lvl_dmg,percent_lvl_hp) VALUES ('{classe}',10,10,10,10);""")
#     else:
#         pass




cursor.execute("SELECT * FROM personagens WHERE user_username = '123';")
print(cursor.fetchall())
# Feche a conexão
conn.close()