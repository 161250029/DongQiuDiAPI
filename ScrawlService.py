import JsonUtil
import NewsSpider
import JSONHandler
import TxtUtil


def get_article_ids(size):
    spider = NewsSpider.NewsSpider()
    article_ids = spider.work_on(size)
    return article_ids

def get_all_comments():
    all_comments = []
    article_ids = get_article_ids()
    for article_id in article_ids:
        for comment in JSONHandler.construct_comments(article_id):
            all_comments.append(comment)
    return all_comments

def dump_comments():
    JsonUtil.dump('comments.json' , get_all_comments())

def dump_user_infos(size):
    all_user_infos = []
    article_ids = get_article_ids(size)
    for article_id in article_ids:
        for user_info in JSONHandler.get_article_user_infos(article_id):
            all_user_infos.append(user_info)
    #print(len(all_user_infos))
    #filter_user_infos = []
    for user_info in all_user_infos:
        if user_info['region'] != None and user_info['hometeam'] != None:
            #filter_user_infos.append(user_info)
            JsonUtil.dump_line("user_info.json" , user_info)
        user_followings = JSONHandler.get_user_following(user_info['id'])
        user_followings_data = user_followings['data']
        TxtUtil.write_line(str(user_info['id']) + " " + str(user_info['username']) + " " + str(user_info['gender']), 'usercontent.txt')
        for u in user_followings_data:
            TxtUtil.write_line(str(user_info['id']) + " " + str(u['id']) , 'relation.txt')
            TxtUtil.write_line(str(u['id']) + " "+ str(u['username']) + " " + str(u['gender']) , 'usercontent.txt')

   # print(len(filter_user_infos))

def get_comments(article_id):
    comments = JSONHandler.construct_comments(article_id)
    return comments


if __name__ == '__main__':
    # comments = get_all_comments()
    # print(comments)
    # print(len(comments))
    dump_user_infos(1)