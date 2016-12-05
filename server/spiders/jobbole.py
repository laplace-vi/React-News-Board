# -*- coding: utf-8 -*-

import requests
from lxml.html import fromstring
from multiprocessing.dummy import Pool as ThreadPool


class Jobbole:
    def __init__(self):
        self.url = 'http://top.jobbole.com/?sort=latest'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.records = []

    @staticmethod
    def get_news_info(element):
        title, href, meta = [''] * 3
        try:
            href = element.cssselect('h3.p-tit a')[0].get('href', '')
            title = element.cssselect('h3.p-tit a')[0].text
            meta = element.cssselect('p.p-meta span')[0].text
        except IndexError:
            pass

        news_info = {
            'title': title,
            'url': href,
            'desc': '',
            'subdesc': meta
        }

        return news_info

    def get_news(self):
        r = requests.get(self.url, headers=self.headers)
        page_source = r.text
        root = fromstring(page_source)
        elements = root.xpath('//li[@class="media"]')

        pool = ThreadPool(8)
        self.records = pool.map(self.get_news_info, elements)
        pool.close()
        pool.join()

        return self.records
