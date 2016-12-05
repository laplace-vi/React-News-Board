# -*- coding: utf-8 -*-

import requests
from lxml.html import fromstring
from multiprocessing.dummy import Pool as ThreadPool


class HackerNews:
    def __init__(self):
        self.url = 'https://news.ycombinator.com/'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.records = []

    @staticmethod
    def get_news_info(element):
        title, href, meta, score, time, comments = [''] * 6
        try:
            href = element.cssselect('a.storylink')[0].get('href', '')
            title = element.cssselect('a.storylink')[0].text
            meta = element.cssselect('span.sitestr')[0].text
            score = element.getnext().cssselect('span.score')[0].text
            time = element.getnext().cssselect('span.age a')[0].text
            comments = element.getnext().cssselect('a')[-1].text
        except IndexError:
            pass

        desc = ''
        subdesc = score + ' | ' + comments + ' | ' + meta + ' | ' + time
        news_info = {
            'title': title,
            'url': href,
            'desc': desc,
            'subdesc': subdesc
        }

        return news_info

    def get_news(self):
        r = requests.get(self.url, headers=self.headers)
        page_source = r.text
        root = fromstring(page_source)
        element_sel = root.cssselect('tr.athing')

        pool = ThreadPool(8)
        self.records = pool.map(self.get_news_info, element_sel)
        pool.close()
        pool.join()

        return self.records
