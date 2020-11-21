import JsonUtil
import NewsSpider
import JSONHandler

def get_article_ids():
    spider = NewsSpider.NewsSpider()
    article_ids = spider.work_on(1)
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

def dump_user_infos():
    all_user_infos = []
    article_ids = get_article_ids()
    for article_id in article_ids:
        for user_info in JSONHandler.get_article_user_infos(article_id):
            all_user_infos.append(user_info)
    print(len(all_user_infos))
    filter_user_infos = []
    for user_info in all_user_infos:
        if user_info['region'] != None and user_info['hometeam'] != None:
            filter_user_infos.append(user_info)
            JsonUtil.dump_line("testuser.json" , user_info)
    print(len(filter_user_infos))

def get_user_infos(article_id):
    user_infos_data = []
    user_infos = JSONHandler.get_article_user_infos(article_id)
    for user_info in user_infos_data:
        user_infos_data.append(user_info)
    return user_infos

def get_comments(article_id):
    comments = JSONHandler.construct_comments(article_id)
    return comments


if __name__ == '__main__':
    # comments = get_all_comments()
    # print(comments)
    # print(len(comments))
    dump_user_infos()