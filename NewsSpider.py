import json
import re

from lxml import etree

import requests


### 抓取懂球帝新闻id
class NewsSpider:

    def __init__(self):

        self.base_url = "https://www.dongqiudi.com/api/app/tabs/web/{}.json"  # 基础url
        self.label_num = [3,4,5,6]  # 新闻标签数字（英超、意甲、德甲、西甲）
        self.start_urls = []  # 爬取的新闻列表页链接
        # 初始url
        for num in self.label_num:
            url = self.base_url.format(num)
            self.start_urls.append(url)
        self.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64'
                  ') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',}

    def get_news_page(self, url):
        # 获取一页新闻列表页内容
        try:
            news_page = requests.get(url, headers=self.headers, timeout=5)
        except requests.exceptions.ReadTimeout:
            return None
        news_dict = json.loads(news_page.text)
        label = news_dict.get('label', '')
        next_page = news_dict.get('next', '')
        articles = news_dict.get('articles', [])
        article_ids = [article.get('id') for article in articles] # 获取当前新闻列表页的所有新闻
        result = {'label': label, 'next_page': next_page, 'articles': articles , 'article_ids': article_ids}
        return result


    # Deperated
    def get_news_detail(self, url):
        """获取新闻详情，使用xpath解析技术"""
        try:
            detail = requests.get(url, headers=self.headers, timeout=5)
        except requests.exceptions.ReadTimeout:
            return None
        html = etree.HTML(detail.text)
        title = html.xpath('//div[@class="detail"]/h1/text()')  # 标题
        author = html.xpath('//div[@class="detail"]/h4/span[@class="name"]/text()')  # 作者
        create_time = html.xpath('//div[@class="detail"]/h4/span[@class="time"]/text()')  # 新闻发布时间
        content = html.xpath('//div[@class="detail"]/div[1]//text()')  # 正文文本内容
        images = html.xpath('//div[@class="detail"]/div[1]//img/@src')  # 所有图片链接
        videos = html.xpath('//div[@class="detail"]/div[1]//div[@class="video"]/@src')  # 所有视频链接

        news_detail = {
            'title': title[0],
            'author': author[0],
            'create_time': create_time[0],
            'content': re.escape(''.join(content)),
            'images': '##'.join(images),
            'videos': '##'.join(videos),

        }
        return news_detail

    def select_url(self, url):
        """筛选需要爬取的新闻链接"""
        if 'https://www.dongqiudi.com/article' in url:
            return 'ok'
        else:
            return None

    # return article_ids
    def work_on(self ,page_size):
        # 设置爬取新闻页的页数
        article_list = []
        for i in range(1, page_size + 1):  # 爬取多少页
            if len(set(self.start_urls)) == 1:  # 判断start_urls里面是否全为None
                break
            for j in range(len(self.start_urls)):  # 遍历start_urls来获取即将请求的列表页
                url = self.start_urls[j]
                if url is None:
                    continue
                a_page = self.get_news_page(url)
                if a_page is None:
                    self.start_urls[j] = None
                    continue
                next_page = a_page.get('next_page')  # 获取当前新闻列表页的下一页的链接
                article_ids = a_page.get('article_ids')
                for article_id in article_ids:
                    article_list.append(article_id)
                # print(a_page.get('article_ids'))
                if next_page:  # 更新url列表
                    self.start_urls[j] = next_page
                else:
                    self.start_urls[j] = None
        return article_list
if __name__ == "__main__":
    spider = NewsSpider()
