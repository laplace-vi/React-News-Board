# -*- coding: utf-8 -*-

import os
from contextlib import contextmanager
from fabric.api import run, env, sudo, prefix, cd, settings, local, lcd
from fabric.colors import green, blue
from fabric.contrib.files import exists


env.hosts = ['deploy@111.222.333.44:12345']
env.password = '12345678'
env.key_filename = '~/.ssh/id_rsa'

# path on server
DEPLOY_DIR = '/home/deploy/www'
PROJECT_DIR = os.path.join(DEPLOY_DIR, 'react-news-board')
CONFIG_DIR = os.path.join(PROJECT_DIR, 'deploy')
LOG_DIR = os.path.join(DEPLOY_DIR, 'logs')
VENV_DIR = os.path.join(DEPLOY_DIR, 'venv')
VENV_PATH = os.path.join(VENV_DIR, 'bin/activate')

# path on local
PROJECT_LOCAL_DIR = '/Users/Ethan/Documents/Code/react-news-board'

GITHUB_PATH = 'https://github.com/ethan-funny/react-news-board'


@contextmanager
def source_virtualenv():
    with prefix("source {}".format(VENV_PATH)):
        yield


def build():
    with lcd("{}/client".format(PROJECT_LOCAL_DIR)):
        local("npm run build")


def deploy():
    print green("Start to Deploy the Project")
    print green("=" * 40)

    # Create directory
    print blue("create the deploy directory")
    print blue("*" * 40)
    mkdir(path=DEPLOY_DIR)
    mkdir(path=LOG_DIR)

    # Get source code
    print blue("get the source code from remote")
    print blue("*" * 40)
    with cd(DEPLOY_DIR):
        with settings(warn_only=True):
            rm(path=PROJECT_DIR)
        run("git clone {}".format(GITHUB_PATH))

    # Install python virtualenv
    print blue("install the virtualenv")
    print blue("*" * 40)
    sudo("apt-get install python-virtualenv")

    # Install nginx
    print blue("install the nginx")
    print blue("*" * 40)
    sudo("apt-get install nginx")
    sudo("cp {}/nginx.conf /etc/nginx/".format(CONFIG_DIR))
    sudo("cp {}/nginx_geekvi.conf /etc/nginx/sites-enabled/".format(CONFIG_DIR))

    # Install python requirements
    with cd(DEPLOY_DIR):
        if not exists(VENV_DIR):
            run("virtualenv {}".format(VENV_DIR))
        with settings(warn_only=True):
            with source_virtualenv():
                sudo("pip install -r {}/requirements.txt".format(PROJECT_DIR))

    # Config supervisor
    sudo("supervisord -c {}/supervisor.conf".format(CONFIG_DIR))
    sudo("supervisorctl -c {}/supervisor.conf reload".format(CONFIG_DIR))
    sudo("supervisorctl -c {}/supervisor.conf status".format(CONFIG_DIR))
    sudo("supervisorctl -c {}/supervisor.conf start all".format(CONFIG_DIR))


def mkdir(sudo_flag=None, path=None):
    mkdir_command = "mkdir {}".format(path)
    if not exists(path):
        if sudo_flag:
            sudo(mkdir_command)
        else:
            run(mkdir_command)


def rm(sudo_flag=None, path=None):
    rm_command = "rm -rf {}".format(path)
    if exists(path):
        if sudo_flag:
            sudo(rm_command)
        else:
            run(rm_command)
