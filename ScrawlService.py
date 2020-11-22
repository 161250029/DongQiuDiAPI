import JsonUtil
import NewsSpider
import JSONHandler
import TxtUtil


def get_article_ids(size):
    spider = NewsSpider.NewsSpider()
    article_ids = spider.work_on(size)
    return article_ids


def dump_comments(size):
    article_ids = get_article_ids(size)
    for article_id in article_ids:
        for comment in JSONHandler.construct_comments(article_id):
            JsonUtil.dump_line('comments.json', comment)

def dump_user_infos(size):
    contains_user_id = []
    article_ids = get_article_ids(size)
    for article_id in article_ids:
        for user_info in JSONHandler.get_article_user_infos(article_id):
            if user_info == None:
                continue
            if user_info['region'] != None and user_info['hometeam'] != None:
                #filter_user_infos.append(user_info)
                JsonUtil.dump_line("new_user_info.json" , user_info)
            user_followings = JSONHandler.get_user_following(user_info['id'])
            user_followings_data = user_followings['data']
            TxtUtil.write_line(str(user_info['id']) + " " + str(user_info['username']) + " " + str(user_info['hometeam']) +
                               " " + str(user_info["created_at"]) + str(user_info['gender']), 'new_usercontent.txt')
            for u in user_followings_data:
                TxtUtil.write_line(str(user_info['id']) + " " + str(u['id']) , 'new_relation.txt')
                TxtUtil.write_line(str(u['id']) + " "+ str(u['username']) + " " + str(u['gender']) , 'new_usercontent.txt')

if __name__ == '__main__':
    # dump_user_infos(50)
    dump_user_infos(1)