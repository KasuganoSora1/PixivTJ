from os import curdir
import pymysql
import configparser
from config import pixivTJ_config

def insert(sql_str):
    sql_str=pretreatment_sql_str(sql_str)
    conn=pymysql.connect(host=pixivTJ_config.get("db","host"),\
        user=pixivTJ_config.get("db","user"),passwd=pixivTJ_config.get("db","pwd"),\
        database=pixivTJ_config.get("db","dbname"))
    cursor=conn.cursor()
    try:
        cursor.execute(sql_str)
        conn.commit()
    except Exception as e:
        raise Exception("sql insert error"+str(e))
    finally:
        cursor.close()
        conn.close()

def isstrexist(table_name,unique_id,id):
    conn=pymysql.connect(host=pixivTJ_config.get("db","host"),\
        user=pixivTJ_config.get("db","user"),passwd=pixivTJ_config.get("db","pwd"),\
        database=pixivTJ_config.get("db","dbname"))
    cursor=conn.cursor()
    try:
        sql_str="select "+unique_id+" from "+table_name+" "+\
            "where "+unique_id+"='"+id+"'"
        sql_str=pretreatment_sql_str(sql_str)
        cursor.execute(sql_str)
        rs=cursor.fetchall()
        length=len(rs)
        if(length==0):
            return True #不存在
        else:
            return False #存在
    except Exception as e:
        raise Exception("sql isexist error")
    finally:
        cursor.close()
        conn.close()

def isstrexist2(table_name,unique_id1,id1,unique_id2,id2):
    conn=pymysql.connect(host=pixivTJ_config.get("db","host"),\
        user=pixivTJ_config.get("db","user"),passwd=pixivTJ_config.get("db","pwd"),\
        database=pixivTJ_config.get("db","dbname"))
    cursor=conn.cursor()
    try:
        sql_str="select "+unique_id1+","+unique_id2+" from "+table_name+" "+\
            "where "+unique_id1+"='"+id1+"' and "+unique_id2+"='"+id2+"'"
        sql_str=pretreatment_sql_str(sql_str)
        cursor.execute(sql_str)
        rs=cursor.fetchall()
        length=len(rs)
        if(length==0):
            return True #不存在
        else:
            return False #存在
    except Exception as e:
        raise Exception("sql isexist error")
    finally:
        cursor.close()
        conn.close()

def pretreatment_sql_str(sql_str):
    return_txt=sql_str.replace("'","\'")
    return return_txt