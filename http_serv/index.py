from flask import Flask
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_restplus import Api, Resource
app = Flask(__name__)
api = Api(app)
@api.route('/helloworld/')
class HelloWorld(Resource):
    def get(self):
        return "Hello Stranger"
    
if __name__ == '__main__':
    app.run()