# -*- encoding: utf-8 -*-

from server import create_app
from flask_script import Manager, Server


manager = Manager(create_app)
manager.add_command('runserver', Server(host='127.0.0.1', port=2345))


if __name__ == '__main__':
    manager.run()
