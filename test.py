import orm
import json
"""
jobject=json.load(open("./tag.json",encoding="utf-8"))
jillust=jobject["illust"]["79019158"]
for key in jobject["illust"]["79019158"]:
    print(key)
    print(type(jobject["illust"]["79019158"][key]))
#orm.write(jillust,"illust")
"""
jobject=json.load(open("./tag.json",encoding="utf-8"))
orm.write(jobject["illust"]["79019158"],"Illust")