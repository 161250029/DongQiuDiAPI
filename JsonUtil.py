import json

# 格式化写入json
def dump(filename , json_str):
    with open(filename , 'w' , encoding='utf-8') as file_obj:
        ## 必须在最终的dump下设置ensure_ascii为false
        json.dump(json_str, file_obj, ensure_ascii=False, indent=4)
        # json.dump(json_str , file_obj)
