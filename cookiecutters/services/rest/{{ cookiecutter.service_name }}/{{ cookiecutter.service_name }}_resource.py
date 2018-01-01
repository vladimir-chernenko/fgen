from flask_restful import Resource, fields, marshal_with


class {{ cookiecutter.service_resource }}List(Resource):
    def get(self):
        pass

    def post(self):
        pass


resource_fields = {
    'text': fields.String,
    'uri': fields.Url('{{ cookiecutter.service_name }}')
}


class {{ cookiecutter.service_resource }}(Resource):

    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return {'text': '{{ cookiecutter.service_resource }} is so cool'}
