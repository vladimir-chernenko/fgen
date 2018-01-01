from flask import Blueprint


{{ cookiecutter.service_name }} = Blueprint('{{ cookiecutter.service_name }}', __name__, template_folder='templates')


@{{ cookiecutter.service_name }}.route('/', defaults={'page': 'index'})
@{{ cookiecutter.service_name }}.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
