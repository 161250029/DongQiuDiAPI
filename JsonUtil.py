import json

# 格式化写入json
def dump(filename , json_str):
    with open(filename , 'w' , encoding='utf-8') as file_obj:
        ## 必须在最终的dump下设置ensure_ascii为false
        json.dump(json_str, file_obj, ensure_ascii=False, indent=4)
        # json.dump(json_str , file_obj)


def dump_line(filename , json_str):
    with  open(filename , 'a' , encoding='utf-8') as file_obj:
        json.dump(json_str , file_obj , ensure_ascii=False)
        file_obj.write("\n")



if __name__ == '__main__':
    dic = {
        "user": {
            "id": 11158131,
            "username": "爱丽丝Y",
            "phone_country": "CN",
            "avatar": "https://img1.qunliao.info/fastdfs5/M00/45/B3/rB8CCl909BOAAiWkAAk_070RU20503.jpg",
            "medal_id": 0,
            "medal_desc": "",
            "gender": "secret",
            "up_total": "8175",
            "following_total": "48",
            "followers_total": "15",
            "post_total": "5",
            "signature": "老二刺螈东方厨 曼联巴黎双料",
            "reply_total": "1251",
            "pendant": [
                {
                    "url": "https://sd.qunliao.info/fastdfs3/M00/B5/75/ChOxM1xC2FWAK5dCAAAmr0XTTPA012.png",
                    "title": "",
                    "type": "fav",
                    "width": 48,
                    "height": 48,
                    "scheme": "",
                    "level": 2
                }
            ],
            "newpendant": [
                {
                    "url": "https://sd.qunliao.info/fastdfs3/M00/B5/75/ChOxM1xC2FWAK5dCAAAmr0XTTPA012.png",
                    "title": "",
                    "type": "fav",
                    "width": 42,
                    "height": 42,
                    "scheme": "",
                    "level": 2,
                    "from": "hometeam"
                }
            ],
            "introduction": "已成为懂球帝651天",
            "hometeam": {
                "channel_id": "1101",
                "name": "曼联",
                "avatar": "https://sd.qunliao.info/fastdfs3/M00/B5/75/ChOxM1xC2FWAK5dCAAAmr0XTTPA012.png",
                "color": "#ffac3548",
                "team_id": "50000515"
            },
            "member_bg_url": "https://img1.qunliao.info/fastdfs4/M00/CB/3D/ChNLkl065HOAWbtUAADnFkzUc7o631.jpg",
            "member_team_url": "",
            "medal_url": "",
            "created_at": "2019-01-29 19:06:23",
            "encrypt_id": "dX5/cml4ZnU=",
            "ext": "{\"vipType\":-1,\"vipAdType\":0}",
            "timeline_total": "1300",
            "relation": "follow",
            "avatar_large": "https://img1.qunliao.info/fastdfs5/M00/45/B3/rB8CCl909BOAAiWkAAk_070RU20503.jpg",
            "team_id": "50000515",
            "team_icon": "https://sd.qunliao.info/fastdfs3/M00/B5/75/ChOxM1xC2FWAK5dCAAAmr0XTTPA012.png",
            "user_id": "11158131",
            "intro_detail": "来自火星  已成为懂球帝<font color=\"#15B139\">651</font>天 获得<font color=\"#15B139\">8175</font>个赞"
        }
    },
    dump_line('testuser.json' , dic)