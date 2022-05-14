from os import curdir
import pymysql
import configparser
from config import pixivTJ_config

def insert(sql_str):
    try:
        conn=pymysql.connect(host=pixivTJ_config.get("db","host"),\
            user=pixivTJ_config.get("db","user"),passwd=pixivTJ_config.get("db","pwd"),\
            database=pixivTJ_config.get("db","dbname"))
        cursor=conn.cursor()
        cursor.execute(sql_str)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        raise Exception("sql insert error")

    
    