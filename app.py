from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')



    #!/usr/bin/python3
import os
from time import time
from flask import Flask
from flask_restx import Resource, Api, reqparse

application = Flask(__name__)
api = Api(application)


parser = reqparse.RequestParser()
parser.add_argument('morning', type=bool, help='Morning greeting')
parser.add_argument('afternoon', type=bool, help='Afternoon greeting')


@api.expect(parser)
@api.route('/hello/<string:name>')
class HelloWorld(Resource):
    def get(self, name):
        args = parser.parse_args(strict=True)
        if args['morning']:
            greeting = 'Good morning'
        elif args['afternoon']:
            greeting = 'Good afternoon'
        else:
            greeting = 'Hello'
        return {greeting: name}


@api.route('/time')
class Time(Resource):
    def get(self):
        return {'timestamp': time()}

if __name__ == '__main__':
    application.run(debug=True, host=os.environ.get('HOST', '0.0.0.0'), port=os.environ.get('FLASK_PORT', 8080))