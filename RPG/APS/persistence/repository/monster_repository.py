from typing import Any, List, Tuple
from dataclasses import dataclass


from infra.db import *
from model.monster import Monster
from persistence.interface.monster_interface import MonsterInterface

@dataclass
class MonsterDTO:
    name : str
    level : int
    health : int
    demage: int

    
class MonsterRepository(MonsterInterface):
    def __init__(self):
        conn, cursor = get_db()

        # Cria a tabela de monstros permitidas
        cursor.execute('''CREATE TABLE IF NOT EXISTS monsters
                        (name TEXT PRIMARY KEY,
                        level INTEGER,
                        health INTEGER,
                        demage INTEGER
                        );''')

        conn.commit()
        
    def insertMonster(self, monster: Monster):
        conn, cursor = get_db()
        
        try:
            statement = f"""SELECT * FROM monsters WHERE name = '{monster.name}';"""
            cursor.execute(statement)
            query = cursor.fetchone()
            
            if query:
                print("Já existe um monstro com esse nome.")
                return None
            print(f'query monster: {query}')
            statement = f"""INSERT INTO monsters (
                        name,
                        level, 
                        health, 
                        demage
                        ) VALUES 
                        ('{monster.name}', {monster.level}, {monster.health}, {monster.damage});"""
            
            cursor.execute(statement)
            conn.commit()
            
            return monster
        
        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
    
    def deleteMonster(self, monster: Monster):
        conn, cursor = get_db()
        
        try:
            statement = "DELETE FROM monsters WHERE name = ?", (monster.name,)
            cursor.execute(statement)
            conn.commit()
        
        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
    
    def getMonsters(self):

        conn, cursor = get_db()
        try:
            statement = f"""SELECT * FROM monsters;"""
            cursor.execute(statement)
            query = cursor.fetchall()
            if not query:
                return None
                
            return [MonsterDTO(q[0], q[1], q[2], q[3]) for q in query]
        
        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
        
            
        