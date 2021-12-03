print("bd подключен!")   

import mariadb
import sys

import random
import time
import sqlite3
import os

put = os.path.dirname(os.path.realpath(__file__)) + "/"#Путь- (part-1)
IP = "127.0.0.1"
#bd = mariadb.connect(user="Crossfire_bot",password="",host="127.0.0.1",port=3306)
pool = mariadb.ConnectionPool(user="Crossfire_bot",password="",host=IP,port=3306,pool_name="web-app",pool_size=1)
#sql = bd.cursor()
try:
    bd = pool.get_connection()
except mariadb.PoolError as e:
    print(f"Error opening connection from pool: {e}")

sql = bd.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS Crossfire_P.mut (uid BIGINT, unaim TEXT, rid BIGINT, runaim TEXT, date TEXT, time TEXT)")
sql.execute("CREATE TABLE IF NOT EXISTS Crossfire_P.w (uid BIGINT, unaim TEXT, rid BIGINT, runaim TEXT)")
sql.execute("CREATE TABLE IF NOT EXISTS Crossfire_P.role (guild_id BIGINT, w1 BIGINT, w2 BIGINT, w3 BIGINT, mut BIGINT, hi BIGINT)")
sql.execute("CREATE TABLE IF NOT EXISTS Crossfire_P.log (log TEXT)")

sql.execute("ALTER TABLE Crossfire_P.log CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci") # Смена кодировки!
sql.execute("ALTER TABLE Crossfire_P.role CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci") # Смена кодировки!
sql.execute("ALTER TABLE Crossfire_P.w CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci") #   Смена кодировки!
sql.execute("ALTER TABLE Crossfire_P.mut CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci") # Смена кодировки!
bd.commit()
print("BD - OK")



from time import strftime, localtime, sleep #Для (Time)
from threading import Thread



def cek_mut(uid):
    sql.execute(f"SELECT uid, uid FROM Crossfire_P.mut WHERE uid = '{uid}'")
    channel_id = sql.fetchall()
    print(channel_id)
    if len(channel_id) == 0:
        return False
    return (True)

def ls_mut():
    sql.execute(f"SELECT uid FROM Crossfire_P.mut")
    channel_id = sql.fetchall()
    print(channel_id)
    if len(channel_id) == 0:
        bd.close()
        return []
    return (channel_id)

def read_mut(uid):
    sql.execute(f"SELECT date, time, rid FROM Crossfire_P.mut WHERE uid = '{uid}'")
    L = sql.fetchall()[0]
    sql.execute(f"SELECT time, uid FROM Crossfire_P.mut WHERE uid = '{uid}'")
    time = L[0]
    date = L[1]
    mut_id = L[2]
    guild_id = read_role_read(mut_id)

    return (time, date, guild_id)

def rm_mut(uid, rid):
    sql.execute(f"DELETE FROM Crossfire_P.mut WHERE uid LIKE '{uid}' and rid LIKE '{rid}'")
    bd.commit()

def add_mut(uid, unaim, rid, runaim, date, time):
    print(uid)
    sql.execute(f"INSERT INTO Crossfire_P.mut VALUES ('{uid}', '{unaim}', '{rid}', '{runaim}', '{date}', '{time}')")
    bd.commit()



def read_w(uid):
    sql.execute(f"SELECT rid, uid FROM Crossfire_P.w WHERE uid = {uid}")
    channel_id = sql.fetchall() # ЕСЛИ БУДЕТ БОЛЬШЕ ОДНОЙ РОЛИ, НУЖНО БУДЕТ ПЕРЕДЕЛАТЬ!!!
    if len(channel_id) == 0:
        return []
    print(f"LLLL {channel_id}")
    return (channel_id)

def rm_w(uid, rid):
    sql.execute(f"DELETE FROM Crossfire_P.w WHERE uid LIKE '{uid}' and rid LIKE '{rid}'")
    bd.commit()

def add_w(uid, unaim, rid, runaim):
    sql.execute(f"INSERT INTO Crossfire_P.w VALUES ('{uid}', '{unaim}', '{rid}', '{runaim}')")
    bd.commit()







def role_read_w(guild_id):
    sql.execute(f"SELECT w1, w2, w3 FROM Crossfire_P.role WHERE guild_id = {guild_id}")
    channel_id = sql.fetchall() # ЕСЛИ БУДЕТ БОЛЬШЕ ОДНОЙ РОЛИ, НУЖНО БУДЕТ ПЕРЕДЕЛАТЬ!!!
    if len(channel_id) == 0:
        return []
    print(f"LLLL {channel_id}")
    return (channel_id[0])

def role_read_mut(guild_id):
    sql.execute(f"SELECT mut FROM Crossfire_P.role WHERE guild_id = {guild_id}")
    channel_id = sql.fetchall() # ЕСЛИ БУДЕТ БОЛЬШЕ ОДНОЙ РОЛИ, НУЖНО БУДЕТ ПЕРЕДЕЛАТЬ!!!
    if len(channel_id) == 0:
        return []
    print(f"LLLL {channel_id}")
    return (channel_id[0][0])


def role_read_hi(guild_id):
    sql.execute(f"SELECT hi FROM Crossfire_P.role WHERE guild_id = {guild_id}")
    channel_id = sql.fetchall() # ЕСЛИ БУДЕТ БОЛЬШЕ ОДНОЙ РОЛИ, НУЖНО БУДЕТ ПЕРЕДЕЛАТЬ!!!
    if len(channel_id) == 0 or channel_id != None:
        return 0
    print(f"LLLL {channel_id}")
    return (channel_id[0][0])



def read_role_read(mut_id):
    sql.execute(f"SELECT guild_id FROM Crossfire_P.role WHERE mut = {mut_id}")
    return (sql.fetchall()[0][0])



    
    
    
