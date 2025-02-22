# from model.user import User
# from model.character import Character
# import sqlite3

# class Database:
#     def __init__(self):
#         # Conecta-se ao banco de dados (cria-o se não existir)
#         self.conn = sqlite3.connect('main.db')

#         # Cria um cursor
#         self.cursor = self.conn.cursor()

#         # Cria a tabela usuarios 
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS user
#                         (username TEXT PRIMARY KEY, password TEXT)''')

        
#         self.conn.commit()
#         self.conn.close()
    
#     # Insere no banco o usuario com nome "username" e senha "password"
#     def insertUser(self, userRef: User):
#         self.conn = sqlite3.connect('main.db')
#         self.cursor = self.conn.cursor()
#         self.cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?", (userRef.username, userRef.password,))
#         user = self.cursor.fetchone()
#         if user is not None:
#             print("Já existe um usuário com esse nome.")
#             self.conn.close()
#             return None
        
#         self.cursor.execute("INSERT INTO user (username, password) VALUES (?, ?)", (userRef.username, userRef.password,))
#         self.conn.commit()
#         self.conn.close()
#         return userRef
     
#     # Deleta o usuario com nome "username"
#     def deleteUser(self, userRef : User):
#         self.conn = sqlite3.connect('main.db')
#         self.cursor = self.conn.cursor()
#         self.cursor.execute("DELETE FROM personagens WHERE user_username = ?", (userRef.username,))
#         self.cursor.execute("DELETE FROM user WHERE username = ?", (userRef.username,))
#         self.conn.commit()
#         self.conn.close()
    
#     def searchUser(self, userRef: User) -> User:
#         self.conn = sqlite3.connect('main.db')
#         self.cursor = self.conn.cursor()
#         self.cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?", (userRef.username, userRef.password))
#         user = self.cursor.fetchone()
#         self.conn.commit()
#         self.conn.close()

#         if user is None :
#             return None
#         else:
#             print(user[0])
#             return User( user[0], user[1] )
        
#     # Retorna todos os personagens de um usuario com nome "username"    
#     def getUserCharacters(self, userRef : User):
#         self.conn = sqlite3.connect('main.db')
#         self.cursor = self.conn.cursor()
#         self.cursor.execute("SELECT * FROM personagens WHERE user_username = ?", (userRef.username,))
#         personagens = self.cursor.fetchall()
#         self.conn.commit()
#         self.conn.close()
#         return personagens
        
#     # Cria um Personagem no banco "Character" que pertence ao usuario "User"
#     def insertCharacter(self, character : Character, userRef : User):
#         self.conn = sqlite3.connect('main.db')
#         self.cursor = self.conn.cursor()
#         self.cursor.execute("SELECT * FROM personagens WHERE nome = ?", (character.name,))
#         char = self.cursor.fetchone()
        
#         if char is not None :
#             print("Um personagem com esse nome já existe !")
#             self.conn.close()
#             return None
        
#         self.cursor.execute("INSERT INTO personagens (nome, classe, user_username) VALUES (?, ?, ?)", (character.name, character._class, userRef.username))
#         self.conn.commit()
#         self.conn.close()
#         return character

#     def deleteCharacter(self, character : Character):
#         self.conn = sqlite3.connect('main.db')
#         self.cursor = self.conn.cursor()
#         self.cursor.execute("DELETE FROM personagens WHERE nome = ?", (character.name,))
#         self.conn.commit()
#         self.conn.close()