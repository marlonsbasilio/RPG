from typing import Any, List, Tuple
from dataclasses import dataclass


from infra.db import *
from model.user import User
from persistence.interface.user_interface import UserInterface

@dataclass
class UserDTO:
    username : str
    password : str
    
class UserRepository(UserInterface):
    def __init__(self):
        conn,cursor = get_db()
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS user
                        (username TEXT PRIMARY KEY, password TEXT)''')
        
        conn.commit()
        close_db(conn)
        
    def insertUser(self, user: User):
        conn,cursor = get_db()
        try:
            statement = f"""SELECT * FROM user 
                            WHERE username = '{user.username}' AND 
                            password = '{user.password}';"""
            cursor.execute(statement)
            query = cursor.fetchone()
            print(query)
            if query:
                print("Já existe um usuário com esse nome.")
                conn.close()
                return None
            
            statement = f"""INSERT INTO user 
                        (username, 
                        password) VALUES 
                        ('{user.username}', '{user.password}');"""
            
            cursor.execute(statement)
            conn.commit()
            
            return user
        
        except Exception as e:
            print(e)
            
        finally:
            close_db(conn)
            
    
    def deleteUser(self,user: User):
        conn,cursor = get_db()
        
        try:
            statement = f"""DELETE FROM personagens WHERE user_username = '{user.username}';"""
            cursor.execute(statement)
            statement = f"""DELETE FROM user WHERE username = '{user.username}';"""
            cursor.execute(statement)
            
            conn.commit()
        
        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
            
            
    def getUser(self, user: User):
        conn,cursor = get_db()
        
        try:
            statement = f"""SELECT * FROM user WHERE username = '{user.username}' AND password = '{user.password}';"""
            cursor.execute(statement)
            query = cursor.fetchone()
            print(f'query: {query}')
            

            if not query :
                return None
                
            return UserDTO(query[0], query[1])

        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
        
        
            
        