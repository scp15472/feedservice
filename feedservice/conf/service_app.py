from flask import Flask
from flask_restful import Api
import django
from feedservice.service_apis.question import Question

django.setup()

app = Flask(__name__)

api = Api(app=app, prefix='/feedservice/')

api.add_resource(Question, 'question')

if __name__ == "__main__":
    app.run(host='localhost', port=2005, debug=True)
