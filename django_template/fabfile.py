# Defines all the actions Fabric cant take.

# lib imports
# django imports
# 3rd party imports
from fabric.api import lcd, local

# app imports


def prepare_deployment(branch_name):
    local('python manage.py test django_template_project')
    local('git add -p && git commit')


def deploy():
    with lcd('/path/to/my/prod/area/'):
        # With git...
        local('git pull /my/path/to/dev/area/')

        # With Mercurial...
        local('hg pull /my/path/to/dev/area/')
        local('hg update')

        # With both
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('/my/command/to/restart/webserver')
