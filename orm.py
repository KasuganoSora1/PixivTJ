import datetime
def write(JObject,tablename):
    into_str =""
    value_str=""
    for key in JObject.keys():
        if(type(JObject[key])==str):
            into_str=into_str+key+","
            value_str=value_str+"'"+JObject[key]+"',"
        elif(type(JObject[key])==bool or type(JObject)==int):
            into_str=into_str+key+","
            value_str=value_str+str(JObject[key])+","
    into_str=into_str.strip(",")
    value_str=value_str.strip(",")
    insert_str="insert into "+tablename+"("+into_str+") values("+value_str+")"
    print(insert_str)
