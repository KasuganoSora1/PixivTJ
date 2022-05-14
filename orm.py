import datetime
import sql
def write(JObject,tablename):
    into_str =""
    value_str=""
    for key in JObject.keys():
        if(key=="urls"):
            urls=JObject["urls"]
            for url_key in urls:
                into_str=into_str+"url_"+url_key+","
                value_str=value_str+"'"+urls[url_key]+"',"
            continue
        if(key=="translation"):
            translation_name=JObject["translation"]["en"]
            into_str=into_str+"translation_name,"
            value_str=value_str+"'"+translation_name+"',"
        if(type(JObject[key])==str):
            into_str=into_str+key+","
            value_str=value_str+"'"+JObject[key]+"',"
        elif(type(JObject[key])==bool or type(JObject)==int):
            into_str=into_str+key+","
            value_str=value_str+str(JObject[key])+","
    into_str=into_str.strip(",")
    value_str=value_str.strip(",")
    insert_str="insert into "+tablename+"("+into_str+") values("+value_str+")"
    sql.insert(insert_str)