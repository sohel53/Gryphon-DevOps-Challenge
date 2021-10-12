from flask import Flask
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', help='Specify your name')


@api.route('/<string:name>/')
class name(Resource):
    @api.doc(parser=parser)
    def get(name):        
        args = parser.parse_args()
        name = args['name']
        return "Hello " + name

@api.route('/helloworld/')
class HelloWorld(Resource):
    def get(self):
        return "Hello Stranger"
    
if __name__ == '__main__':
    app.run()