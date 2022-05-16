import json
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