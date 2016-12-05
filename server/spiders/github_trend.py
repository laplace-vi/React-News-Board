# -*- coding: utf-8 -*-

import requests
from lxml.html import fromstring
from multiprocessing.dummy import Pool as ThreadPool


class GitHubTrend(object):
    def __init__(self):
        self.url = 'https://github.com/trending'
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = {'User-Agent': self.user_agent}
        self.records = []

    def _get_page_source(self, url):
        r = requests.get(url, headers=self.headers)
        page_source = r.text
        return page_source

    @staticmethod
    def _get_trend_info(repo):
        name, desc, lang, today_stars, all_stars, url, subdesc = [''] * 7

        name_xpath = ".//h3/a"
        desc_xpath = ".//p[@class='col-9 d-inline-block text-gray m-0 pr-4']"
        lang_xpath = "./div[@class='f6 text-gray mt-2']/span[@class='mr-3']"
        today_stars_xpath = "./div[@class='f6 text-gray mt-2']/span[@class='float-right']"  # NOQA
        all_stars_xpath = "./div[@class='f6 text-gray mt-2']/a"

        try:
            name = repo.xpath(name_xpath)[0].xpath('string(.)')
            name = ''.join(name.split())
            url = 'https://github.com/' + name
        except IndexError:
            pass

        try:
            lang = repo.xpath(lang_xpath)[0].xpath('string(.)').strip()
        except IndexError:
            pass

        try:
            today_stars = repo.xpath(today_stars_xpath)[0].xpath('string(.)').strip()  # NOQA
        except IndexError:
            pass

        try:
            all_stars = repo.xpath(all_stars_xpath)[0].xpath('string(.)').strip()  # NOQA
            all_stars += ' stars total'
        except IndexError:
            pass

        try:
            desc = repo.xpath(desc_xpath)[0].xpath('string(.)').strip()
        except IndexError:
            pass

        subdesc = ' | '.join(filter(bool, [lang, today_stars, all_stars]))

        trend_info = {
            'title': name,
            'url': url,
            'desc': desc,
            'subdesc': subdesc,
        }

        return trend_info

    def get_trend_list(self):
        page_source = self._get_page_source(self.url)
        root = fromstring(page_source)
        repo_list = root.xpath(
            "//li[@class='col-12 d-block width-full py-4 border-bottom']"
        )

        pool = ThreadPool(8)
        self.records = pool.map(self._get_trend_info, repo_list)
        pool.close()
        pool.join()

        return self.records
