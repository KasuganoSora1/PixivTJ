import json
import orm
import sql
def is_exist_json(txt):
    pre_search_start=txt.find("preload-data")
    if(pre_search_start==-1):
        return False
    else:
        return True
def get_json(txt):
    try:
        pre_search_start=txt.find("preload-data")+1
        search_start=txt.find("'",pre_search_start)
        search_end=txt.find("'",search_start+2)
        json_txt=txt[search_start+1:search_end]
        result_json=json.loads(json_txt)
        return json.loads(json_txt)
    except Exception as e:
        raise Exception("txt trans json error")

def write_from_html_txt(html_txt,id):
    if(is_exist_json(html_txt)):
        jobject=get_json(html_txt)
        #---insert illust
        for ikey in jobject["illust"]:
            if(sql.isstrexist("illust","illustid",ikey)):
                iobject=jobject["illust"][ikey]
                orm.write(iobject,"illust")
            for tobject in jobject["illust"][ikey]["tags"]["tags"]:
                if(sql.isstrexist("tag","tag",tobject["tag"])):
                    orm.write(tobject,"tag")
                if(sql.isstrexist2("illusttag","illustid",ikey,"tag",tobject["tag"])):
                    illust_tag={
                        "illustid":ikey,
                        "tag":tobject["tag"]
                    }
                    orm.write(illust_tag,"illusttag")
        for ukey in jobject["user"]:
            if(sql.isstrexist("user","userId",ukey)):
                orm.write(jobject["user"][ukey],"user")
    else:
        if(sql.isstrexist("ErrorIllust","illustId",id)):
            jo={
                "illustId":id,
                "reason":"notexist"
            }
            orm.write(jo,"ErrorIllust")
