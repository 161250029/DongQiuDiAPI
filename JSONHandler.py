import json
import JsonUtil

import requests
# 解析json字符串

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64'
                  ') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}

def construct_comments(article_id):
    url = "https://api.dongqiudi.com/v2/article/" + str(article_id) + "/comment?size=1000&version=1&platform=h5"
    # print(url)
    json_data = requests.get(url , headers=headers)
    data = json.loads(json_data.text)
    article_data = data['data']
    comment_list = article_data['comment_list']
    print(json.dumps(comment_list))
    print(json.dumps(comment_list , ensure_ascii=False))
    JsonUtil.dump('test.json' , json.dumps(comment_list , ensure_ascii=False))
    # comment_content = [coment.get("content") for coment in comment_list]
    # print(comment_content)
    # print(len(comment_content))
    return comment_list



def construct_user_ids(article_id):
    comment_list = construct_comments(article_id)
    user_ids = []
    for comment in comment_list:
        user_ids.append(comment['user_id'])
    return user_ids



def get_article_user_infos(article_id):
    user_ids = construct_user_ids(article_id)
    aricle_user_infos = []
    for user_id in user_ids:
        aricle_user_infos.append(get_user_info(user_id))
    return aricle_user_infos


def get_user_info(user_id):
    url = "https://api.dongqiudi.com/users/profile/" +user_id + "?version=230&platform=android"
    user_json_data = requests.get(url , headers = headers)
    user_info = json.loads(user_json_data.text)
    user_real_info = user_info['user']
    new_user_info_dic = {}
    new_user_info_dic["id"] = user_real_info["id"]
    new_user_info_dic["created_at"] = user_real_info["created_at"]
    new_user_info_dic["username"] = user_real_info["username"]
    new_user_info_dic["gender"] = user_real_info["gender"]
    region = user_real_info["region"]
    if region == None:
        new_user_info_dic["region"] = None
    else:
        new_user_info_dic["region"] = region["phrase"]
    hometeam = user_real_info["hometeam"]
    new_user_info_dic["hometeam"] = hometeam["name"]
    return new_user_info_dic

def get_user_following(user_id):
    url = "https://api.dongqiudi.com/user/following/" + user_id
    user_following_infos = {}
    user_json_following_data = requests.get(url, headers=headers)
    user_following_data = json.loads(user_json_following_data.text)
    user_following_infos['userid'] = user_id
    user_following_infos['total'] = user_following_data['total']
    user_following_infos['data'] = user_following_data['data']
    return user_following_infos

def get_user_follower(user_id):
    url = "https://api.dongqiudi.com/user/followers/" + user_id
    user_follower_dic = {}
    user_json_follower_data = requests.get(url , headers=headers)
    user_follower_data = json.loads(user_json_follower_data.text)
    return user_follower_data

if __name__ == '__main__':
    # construct_comments('1669701')
    # print(construct_comments('1669701'))


    # JsonUtil.dump('user.json' , json.dumps(get_user_info('13484027')))
    # print(get_user_info('13484027'))

    print(get_user_following('13484027'))
    print(get_user_follower('13484027'))

    # print(get_article_user_infos("1667029"))
