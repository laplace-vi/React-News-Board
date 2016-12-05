# -*- coding: utf-8 -*-

import flask
from flask import jsonify

from server.spiders.github_trend import GitHubTrend
from server.spiders.toutiao import Toutiao
from server.spiders.hacker_news import HackerNews
from server.spiders.segmentfault import SegmentFault
from server.spiders.jobbole import Jobbole

news_bp = flask.Blueprint(
    'news',
    __name__,
    url_prefix='/api'
)


@news_bp.route('/github/repo_list', methods=['GET'])
def get_github_trend():
    gh_trend = GitHubTrend()
    gh_trend_list = gh_trend.get_trend_list()

    return jsonify(
        message='OK',
        data=gh_trend_list
    )


@news_bp.route('/toutiao/posts', methods=['GET'])
def get_toutiao_posts():
    toutiao = Toutiao()
    post_list = toutiao.get_posts()

    return jsonify(
        message='OK',
        data=post_list
    )


@news_bp.route('/hacker/news', methods=['GET'])
def get_hacker_news():
    hacker = HackerNews()
    news_list = hacker.get_news()

    return jsonify(
        message='OK',
        data=news_list
    )


@news_bp.route('/segmentfault/blogs', methods=['GET'])
def get_segmentfault_blogs():
    sf = SegmentFault()
    blogs = sf.get_blogs()

    return jsonify(
        message='OK',
        data=blogs
    )


@news_bp.route('/jobbole/news', methods=['GET'])
def get_jobbole_news():
    jobbole = Jobbole()
    blogs = jobbole.get_news()

    return jsonify(
        message='OK',
        data=blogs
    )
