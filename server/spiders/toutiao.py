# -*- coding: utf-8 -*-

import requests
from lxml.html import fromstring
from multiprocessing.dummy import Pool as ThreadPool


class Toutiao:
    def __init__(self):
        self.url = 'https://toutiao.io/'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.records = []

    def _get_page_source(self, url):
        r = requests.get(url, headers=self.headers)
        page_source = r.text
        return page_source

    def _get_origin_url(self, url):
        if 'toutiao' not in url:
            url = 'https://toutiao.io' + url

        r = requests.get(url, headers=self.headers, allow_redirects=False)
        page_source = r.text
        root = fromstring(page_source)
        href = ''
        try:
            post_href = root.cssselect('a')[0].get('href')
            post_href_list = post_href.split('?')
            if len(post_href_list) > 1 and 'toutiao' in post_href_list[1]:
                href = post_href_list[0]
            else:
                href = post_href
        except Exception:
            pass

        return href

    def _get_post_info(self, element):
        toutiao_href, title, meta, href = [''] * 4
        try:
            toutiao_href = element.cssselect('h3 a')[0].get('href')
            href = self._get_origin_url(toutiao_href)
            title = element.cssselect('h3 a')[0].text
            meta = element.cssselect('div.meta')[0].text.strip()
        except Exception as e:
            print e

        posts_info = {
            'title': title,
            'url': href,
            'desc': '',
            'subdesc': meta
        }

        return posts_info

    def get_posts(self):
        page_source = self._get_page_source(self.url)
        root = fromstring(page_source)
        element_sel = root.cssselect('div.post div.content')

        pool = ThreadPool(8)
        self.records = pool.map(self._get_post_info, element_sel)
        pool.close()
        pool.join()

        return self.records
