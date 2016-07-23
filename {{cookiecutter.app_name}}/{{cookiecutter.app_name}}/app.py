from flask import Flask
from flask_restful import Api
from {{cookiecutter.app_name}}.resources.foo import Foo
from {{cookiecutter.app_name}}.resources.bar import Bar
from {{cookiecutter.app_name}}.resources.baz import Baz

app = Flask(__name__)
api = Api(app)

api.add_resource(Foo, '/Foo', '/Foo/<str:id>')
api.add_resource(Bar, '/Bar', '/Bar/<str:id>')
api.add_resource(Baz, '/Baz', '/Baz/<str:id>')
