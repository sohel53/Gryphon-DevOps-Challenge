from flask import Flask , json
import requests
import subprocess
import datetime
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api, Resource, reqparse, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Configure Http Server',
    description='Completing DevOps challenge',
)

@api.route('/helloworld/')
class HelloWorld(Resource):
    def get(self):
        return "Hello stranger", 201

parser = reqparse.RequestParser()
parser.add_argument('name', help='Specify your name')

@api.route('/hello/')
class HelloWorld(Resource):
    @api.doc(parser=parser)
    def get(self):        
        args = parser.parse_args()
        name = args['name']
        return "Hello " + name, 201

@api.route('/versionz/')
class HelloWorld(Resource):
  def get(self):
    full_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    full_hash = str(full_hash, "utf-8").strip()
    return full_hash, 201

if __name__ == '__main__':
    api.run(debug=True)