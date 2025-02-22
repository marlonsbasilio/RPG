from typing import Any, List, Tuple
from dataclasses import dataclass


from infra.db import *
from model.classe import Classe
from persistence.interface.classe_interface import ClasseInterface

@dataclass
class ClasseDTO:
    classe : str
    base_dmg : int
    base_hp : int
    percent_lvl_dmg: int
    percent_lvl_hp: int
    
class ClasseRepository(ClasseInterface):
    def __init__(self):
        conn, cursor = get_db()

        # Cria a tabela de classes permitidas
        cursor.execute('''CREATE TABLE IF NOT EXISTS classes
                        (classe TEXT PRIMARY KEY,
                        base_dmg INTEGER,
                        base_hp INTEGER,
                        percent_lvl_dmg INTEGER,
                        percent_lvl_hp INTEGER);''')
        classes = ['Sacerdote']
        for classe in classes:
            cursor.execute(f"""SELECT * FROM classes WHERE classe = '{classe}';""")
            resultado = cursor.fetchone()
            print(classe)
            if not resultado:
                cursor.execute(f"""INSERT INTO classes (classe,base_dmg,base_hp,percent_lvl_dmg,percent_lvl_hp) VALUES ('{classe}',10,10,10,10);""")
            else:
                pass

        conn.commit()
        
    def insertClasse(self, classe: Classe):
        conn, cursor = get_db()
        
        try:
            statement = "SELECT * FROM user WHERE classe = ?", (classe.classe)
            cursor.execute(statement)
            query = cursor.fetchone()
            
            if query:
                print("Já existe uma classe com esse nome.")
                return None
            
            statement = """INSERT INTO user (
                        classe,
                        base_dmg, 
                        base_hp, 
                        percent_lvl_dmg,
                        percent_lvl_hp) VALUES 
                        (?, ?, ?, ?)""", (classe.classe, classe.base_dmg, classe.base_hp, classe.percent_lvl_dmg, classe.percent_lvl_hp)
            
            cursor.execute(statement)
            conn.commit()
            
            return classe
        
        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
    
    def deleteClasse(self, classe: Classe):
        conn, cursor = get_db()
        
        try:
            statement = "DELETE FROM personagens WHERE classe = ?", (classe.classe,)
            cursor.execute(statement)
            statement = "DELETE FROM classe WHERE classe = ?", (classe.classe,)
            conn.commit()
        
        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
            
    def getAllowedClasses(self):
        conn, cursor = get_db()
        
        try:
            statement = f"SELECT * FROM classes;"
            cursor.execute(statement)
            query = cursor.fetchall()
            print(f'query: {query}')

            if not query:
                return None
                
            return [ClasseDTO(q[0], q[1], q[2], q[3], q[4]) for q in query]

        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)

    def getClasse(self,nome):
        conn, cursor = get_db()
        
        try:
            statement = f"SELECT * FROM classes WHERE classe = '{nome}';"
            cursor.execute(statement)
            query = cursor.fetchone()
            print(f'query classe: {query}')

            if not query:
                return None
                
            return ClasseDTO(query[0], query[1], query[2], query[3], query[4])

        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
        
        
            
        