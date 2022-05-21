import pymysql
import requests
from config import pixivTJ_config
import orm
import txt
import sql

def get_txt(this_url):
    #p=pixivTJ_config.get("web","proxy")
    res=requests.get(url=this_url,proxies={
        "http":pixivTJ_config.get("proxy","http"),
        "https":pixivTJ_config.get("proxy","http")
        })
    res_txt=res.text
    res.close()
    return res_txt

def write_from_page_id(id):
    try:
        page_txt=get_txt("https://www.pixiv.net/artworks/"+id)
        txt.write_from_html_txt(page_txt,id)
    except pymysql.Error as sql_err:
         if(sql.isstrexist("ErrorIllust","illustid",id)):
            jo={
                "illustId":id,
                "reason":"INSERTERROR",
                "detail":str(sql_err)
            }
            orm.write(jo,"ErrorIllust")
       
    except requests.Timeout as timeout_err:
        if(sql.isstrexist("ErrorIllust","illustid",id)):
            jo={
                "illustId":id,
                "reason":"TIMEOUTERROR",
                "detail":str(timeout_err)
            }
            orm.write(jo,"ErrorIllust")
    except Exception as err:
        if(sql.isstrexist("ErrorIllust","illustid",id)):
            jo={
                "illustId":id,
                "reason":"UNKNOWNERROR",
                "detail":str(err)
            }
            orm.write(jo,"ErrorIllust")
    