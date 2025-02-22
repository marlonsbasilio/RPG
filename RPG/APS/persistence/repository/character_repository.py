from typing import Any, List, Tuple
from dataclasses import dataclass


from infra.db import *
from model.character import Character
from model.classe import Classe
from model.user import User
from persistence.interface.character_interface import CharacterInterface

@dataclass
class characterDTO:
    name: str
    _class: Classe
    user: User
    level: int
    health: int
    exp: int
    damage: int
    
class CharacterRepository(CharacterInterface):
    def __init__(self):
        conn, cursor = get_db()

        cursor.execute('''CREATE TABLE IF NOT EXISTS personagens
                  (nome TEXT PRIMARY KEY, 
                  classe TEXT, 
                  user_username TEXT,
                  level INTEGER,
                  health INTEGER,
                  exp INTEGER,
                  damage INTEGER,
                  FOREIGN KEY(user_username) REFERENCES user(username),
                  FOREIGN KEY(classe) REFERENCES classes(classe))''')

        conn.commit()
        
    def insertCharacter(self, character: Character):

        conn, cursor = get_db()
        
        try:
            print(f'char name:{character.name}')
            statement = f"""SELECT * FROM personagens WHERE nome = '{character.name}';"""
            cursor.execute(statement)
            query = cursor.fetchone()
            print(query)
            if query:
                print("Já existe personagem com esse nome.")
                return None
            print(f'repo char insert:{character.user.username}')
            statement = f"""INSERT INTO personagens (
                        nome,
                        classe, 
                        user_username, 
                        level,
                        health,
                        exp,
                        damage) VALUES 
                        ('{character.name}', '{character._class.classe}', '{character.user.username}', '{character.level}', '{character.health}', '{character.exp}', '{character.damage}');"""
            
            cursor.execute(statement)
            conn.commit()
            
            return character
        
        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
    
    def deleteUserCharacter(self, character: Character):
        conn, cursor = get_db()
        
        try:
            statement = f"""DELETE FROM personagens WHERE nome = '{character.name}';"""
            cursor.execute(statement)
            conn.commit()
        
        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
            
    def getUserCharacters(self,  userRef : User):
        conn, cursor = get_db()
        print(f'repo char: {userRef.username}')
        try:
            statement = f"""SELECT * FROM personagens WHERE user_username = '{userRef.username}';"""
            cursor.execute(statement)
            query = cursor.fetchall()
            print(f'query repo char: {query}')
            if not query:
                return None
                
            return [characterDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6]) for q in query]
        
        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
    
    def charLevelUp(self, character: Character):
        conn, cursor = get_db()
        try:
            statement = f"""UPDATE personagens
                        SET level = {character.level}
                        WHERE user = '{character.user}';"""
            cursor.execute(statement)
            conn.commit()
        except Exception as e:
            print(e)        
        finally:
            close_db(conn)


    def charUpdate(self, character: Character):
        conn, cursor = get_db()
        try:
            statement = """
                UPDATE personagens
                SET nome = ?, 
                    classe = ?, 
                    user_username = ?, 
                    level = ?, 
                    health = ?, 
                    exp = ?, 
                    damage = ?
                WHERE user_username = ?;
            """
            cursor.execute(statement, (
                character.name, 
                character._class.classe, 
                character.user,  # Aqui, usamos character.user diretamente
                character.level, 
                character.health, 
                character.exp, 
                character.damage, 
                character.user  # Aqui também usamos character.user
            ))
            conn.commit()
        except Exception as e:
            print(f"Erro ao atualizar personagem: {e}")
        finally:
            close_db(conn)



    
    # def charUpdate(self, character: Character):
    #     conn, cursor = get_db()
    #     try:
    #         statement = f"""UPDATE personagens
    #                     SET level = {character.level}
    #                     WHERE user = '{character.user.username}';"""
    #         cursor.execute(statement)
    #         conn.commit()
    #     except Exception as e:
    #         print(e)        
    #     finally:
    #         close_db(conn)


    # conn, cursor = get_db()
    # try:
    #     statement = f"""
    #         UPDATE personagens
    #         SET nome = '{character.name}',
    #             classe = '{character._class.classe}',
    #             user_username = '{character.user.username}',
    #             level = {character.level},
    #             health = {character.health},
    #             exp = {character.exp},
    #             damage = {character.damage}
    #         WHERE user_username = '{character.user.username}';
    #     """
    #     cursor.execute(statement)
    #     conn.commit()
    # except Exception as e:
    #     print(e)
    # finally:
    #     close_db(conn)