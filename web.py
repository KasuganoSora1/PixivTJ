import requests
from config import pixivTJ_config
import orm
import txt

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
    except Exception as e:
        print("error"+str(e))
    