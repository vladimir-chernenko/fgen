import exceptions
import os

import click
import yaml
from cookiecutter.main import cookiecutter
from utils import file_writer, j


# create base flask app
# create service (blueprint)
    # mvc
    # rest service
    # celery worker


@click.command()
@click.option('--app-name', prompt=True)
def create_base_app(app_name):
    click.echo('Creating flask base application')
    FLASK_BASE = '/Users/vladimirchernenko/Documents/gen/cookiecutters/flask-base'
    cookiecutter(os.path.abspath(FLASK_BASE), extra_context={'app_name': app_name}, no_input=True)


@click.command()
@click.option('--service-name', prompt=True)
@click.option('--service-type', type=click.Choice(['rest', 'celery', 'mvc']))
@click.option('--project-path', prompt=True)
def add_service(service_name, service_type, project_path):
    click.echo('Creating flask service {}'.format(service_name))

    project_path = os.path.abspath(project_path)
    application_path = j(project_path, 'application')
    run_py_path = j(project_path, 'run.py')

    if not (os.path.exists(application_path) and os.path.exists(run_py_path)):
        raise NoProjectFound('Project Path: {}'.format(project_path))

    SERVICES_BASE_DIR = '/Users/vladimirchernenko/Documents/gen/cookiecutters/services'
    application_servises_path = j(application_path, 'services')

    if os.path.exists(j(application_servises_path, service_name)):
        raise ServiceAlreadyExists(service_name)

    cookiecutter(
        os.path.abspath(j(SERVICES_BASE_DIR, service_type)),
        output_dir=application_servises_path,
        no_input=True,
        extra_context={'service_name': service_name}
    )

    SERVICE_TYPES = {
        'mvc': post_add_mvc,
        'rest': post_add_rest,
        'celery': post_add_celery
    }

    application_py_path = j(application_path, 'application.py')
    SERVICE_TYPES[service_type](application_py_path, service_name)


def post_add_mvc(application_py_path, service_name):
    text_dict = {
        'start': [
            'from application.services.{name} import {name}'.format(name=service_name)
        ],
        '# FGEN register blueprints': [
            '\tapp.register_blueprint({name}, url_prefix=\'/{name}\')'.format(name=service_name)
        ]
    }
    file_writer(application_py_path, text_dict)


def post_add_rest(application_py_path, service_name):
    text_dict = {
        'start': [
            'from flask_restful import Api'
        ],
        '# FGEN rest api register app': [
            '\tapi = Api(app)'
        ],
        '# FGEN rest api register resources': [
            '\tapi.add_resource({}, \'/{}\')'.format(service_name.title(), service_name)
        ]
    }
    file_writer(application_py_path, text_dict)


def post_add_celery(application_py_path, service_name):
    pass


# if __name__ == '__main__':
    # create_base_app()
    # add_service()
