
import sqlite3

def get_db():
    conn = sqlite3.connect('C:\\Users\\Marlon-PC\\Desktop\\TP2_APS\\tp2-aps\\APS\\main.db')
    # conn = sqlite3.connect('/home/alessandro.dangelo/Documentos/tp2-aps/APS/main.db')
    
    cur = conn.cursor()
    return conn,cur

def close_db(conn):
    conn.close()