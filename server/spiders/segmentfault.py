# -*- coding: utf-8 -*-

import requests
from lxml.html import fromstring
from multiprocessing.dummy import Pool as ThreadPool


class SegmentFault:
    def __init__(self):
        self.url = 'https://segmentfault.com/blogs'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.records = []

    @staticmethod
    def get_blog_info(element):
        title, href, excerpt, meta = [''] * 4
        try:
            href = element.cssselect('h2.title a')[0].get('href', '')
            href = 'https://segmentfault.com' + href
            title = element.cssselect('h2.title a')[0].text
            excerpt = element.cssselect('p.excerpt.wordbreak.hidden-xs')[0].text
            meta = element.cssselect('ul.author.list-inline li')[-1].\
                xpath('string(.)').strip()
            meta = ' '.join(meta.split())

        except Exception as e:
            print e

        blog_info = {
            'title': title,
            'url': href,
            'desc': excerpt,
            'subdesc': meta
        }

        return blog_info

    def get_blogs(self):
        r = requests.get(self.url, headers=self.headers)
        page_source = r.text
        root = fromstring(page_source)
        element_sel = root.cssselect('section.stream-list__item')

        pool = ThreadPool(8)
        self.records = pool.map(self.get_blog_info, element_sel)
        pool.close()
        pool.join()

        return self.records
