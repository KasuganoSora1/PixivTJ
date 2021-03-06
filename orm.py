import datetime
import sql
import time
def write(JObject,tablename):
    into_str =""
    value_str=""
    for key in JObject.keys():
        if((key=="createDate" or key=="uploadDate") and JObject[key]!=None):
            into_str=into_str+key+","
            #value_str=value_str+str(JObject[key])+","
            t=datetime.datetime.strptime(JObject[key],"%Y-%m-%dT%H:%M:%S+00:00")
            t_str=t.strftime("%Y-%m-%d %H:%M:%S")
            value_str=value_str+"'"+t_str+"',"
            continue
        if(key=="restrict" and JObject[key]!=None):
            into_str=into_str+"pixiv_restrict,"
            value_str=value_str+str(JObject[key])+","
            continue
        if(key=="urls" and JObject[key] != None):
            urls=JObject["urls"]
            for url_key in urls:
                into_str=into_str+"url_"+url_key+","
                value_str=value_str+"'"+urls[url_key]+"',"
            continue
        if(key=="translation" and JObject[key] != None):
            translation_name=JObject["translation"]["en"]
            into_str=into_str+"translation_name,"
            value_str=value_str+"'"+translation_name+"',"
            continue
        if(type(JObject[key])==str):
            into_str=into_str+key+","
            value_str=value_str+"'"+JObject[key]+"',"
        elif(type(JObject[key])==bool or type(JObject[key])==int):
            into_str=into_str+key+","
            value_str=value_str+str(JObject[key])+","
    into_str=into_str.strip(",")
    value_str=value_str.strip(",")
    insert_str="insert into "+tablename+"("+into_str+") values("+value_str+")"
    sql.insert(insert_str)

def update(JObject,tablename,unique_key,unique_value):
    update_str =""
    for key in JObject.keys():
        if(type(JObject[key])==str):
            update_str=update_str+key+"='"+JObject[key]+"',"
        elif(type(JObject[key])==bool or type(JObject[key])==int):
            update_str=update_str+key+"="+str(JObject[key])+","
    update_str=update_str.strip(",")
    insert_str=""
    if(type(unique_value)==str):
        insert_str="update "+tablename+" set "+update_str+" where "+unique_key+"='"+unique_value+"'"
    else:
        insert_str="update "+tablename+" set "+update_str+" where "+unique_key+"="+str(unique_value)
    sql.insert(insert_str)