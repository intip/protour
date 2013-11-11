#!/usr/bin/env python
#-*- coding:utf-8 -*-
from fabric.api import env, run, cd, sudo


# if not hasattr(env, "server"):
#     env.server = "69"

# # Usar fab <command> --set server=aws para executar no ec2
# if env.server == "aws":
#     env.hosts = ['deploy@54.221.250.149']
#     env.password = "depl0y"

#     CLONE_PATH = u'/home/deploy/iesb/'
#     PROJECT_PATH = u'/home/deploy/iesb/project'
#     PYTHON_BIN = u'/home/deploy/.venvs/iesb/bin/python'
#     PIP_BIN = u'/home/deploy/.venvs/iesb/bin/pip'
#     WEBSERVER = u'nginx'

# else:
env.hosts = ['deploy@192.168.1.69']
env.password = "depl0y"

CLONE_PATH = u'/home/deploy/protour/'
PROJECT_PATH = u'/home/deploy/protour/project'
PYTHON_BIN = u'/home/deploy/.virtualenvs/protour/bin/python'
PIP_BIN = u'/home/deploy/.virtualenvs/protour/bin/pip'
WEBSERVER = u'httpd'


def pull():
    git("pull --rebase")


def restart():
    sudo("supervisorctl restart protour")
    sudo("service %s restart" % WEBSERVER)


def start():
    sudo("supervisorctl start protour")
    sudo("service %s restart" % WEBSERVER)


def stop():
    sudo("supervisorctl stop protour")


def collectstatic():
    manage('collectstatic --noinput')


def installwatson():
    manage('installwatson')


def buildwatson():
    manage('buildwatson')


def deploy():
    pull()
    install_requirements()
    manage('syncdb --noinput')
    manage('migrate --all')
    buildwatson()
    collectstatic()
    restart()


def fastdeploy():
    pull()
    restart()


def git(cmd):
    with cd(CLONE_PATH):
        run("git %s" % cmd)


def manage(args):
    with cd(CLONE_PATH):
        run("%s manage.py %s" % (PYTHON_BIN, args))


def install_requirements():
    with cd(PROJECT_PATH):
        run("%s install -M -r requirements.txt" % PIP_BIN)


def rm_fb_versions():
    manage('fb_version_remove')


def gen_fb_versions():
    manage('fb_version_generate')
