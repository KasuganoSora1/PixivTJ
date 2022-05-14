import orm
import json
import sql
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

jobject=json.load(open("./tag.json",encoding="utf-8"))
for tag in jobject["illust"]["79019158"]["tags"]["tags"]:
    if (sql.isstrexist("tag","tag",tag["tag"])):
        print("不存在 插入")
        orm.write(tag,"tag")
    else:
        print("已存在 不插入")
#orm.write(jobject["illust"]["79019158"]["tags"]["tags"][0],"tag")


