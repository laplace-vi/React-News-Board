# -*- coding: utf-8 -*-


class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = 'The quick brown fox jumps over the lazy dog'


class DevConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


config_map = {
    'dev': DevConfig,
    'prod': ProductionConfig,
}
