from concurrent.futures import ThreadPoolExecutor
import orm
import json
import sql
import web
import txt
"""
jobject=json.load(open("./tag.json",encoding="utf-8"))
jillust=jobject["illust"]["79019158"]
for key in jobject["illust"]["79019158"]:
    print(key)
    print(type(jobject["illust"]["79019158"][key]))
#orm.write(jillust,"illust")
"""

"""
jobject=json.load(open("./tag.json",encoding="utf-8"))
orm.write(jobject["illust"]["79019158"],"Illust")
"""

"""
jobject=json.load(open("./tag.json",encoding="utf-8"))
orm.write(jobject["user"]["9169975"],"user")
"""

"""
jobject=json.load(open("./tag.json",encoding="utf-8"))
for tag in jobject["illust"]["79019158"]["tags"]["tags"]:
    orm.write(tag,"tag")
#orm.write(jobject["illust"]["79019158"]["tags"]["tags"][0],"tag")
"""

"""
jobject=json.load(open("./tag.json",encoding="utf-8"))
for tag in jobject["illust"]["79019158"]["tags"]["tags"]:
    if (sql.isstrexist("tag","tag",tag["tag"])):
        print("不存在 插入")
        orm.write(tag,"tag")
    else:
        print("已存在 不插入")
#orm.write(jobject["illust"]["79019158"]["tags"]["tags"][0],"tag")
"""

"""
b=web.get_txt("https://www.pixiv.net/artworks/97695147")
print(txt.is_exist_json(b))
json=txt.get_json(b)
pass
"""
"""
for i in range(1,2000):
    t=web.get_txt("https://www.pixiv.net/artworks/"+str(i))
    if(txt.is_exist_json(t)):
        j=txt.get_json(t)
        orm.write(j,"illusion")
    else:
        print(str(i)+"不存在")
"""
"""
for i in range(1,1000):
    t=web.get_txt("https://www.pixiv.net/artworks/"+str(i))
    txt.html_page(t)
"""
pool=ThreadPoolExecutor(max_workers=10)
for i in range(1,1000):
    print("put "+str(i))
    pool.submit(web.write_from_page_id,str(i))