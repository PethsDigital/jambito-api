from data import getData
from flask import Flask  # jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
data = getData()


def searchByCourse(search):
    data, search = getData(), search.upper()
    realData = data['results']
    # print(str(data), realData)
    courses = realData.keys()
    data = {
        'results': {
            course: realData[course]
            for course in courses
            if search in course
        }
    }
    print(type(str(data)))
    return data


def searchBySubject(search):
    data = getData()
    realData = data['results']
    courses = realData.keys()
    data = {
        'results': {
            course: realData[course]
            for course in courses
            if search.lower() in str(realData[course]).lower()
        }
    }
    return data


class Index(Resource):
    def get(self):
        return data


class SeearchByCourse(Resource):

    def get(self, search):
        data = searchByCourse(search)
        return data


class SeearchBySubject(Resource):

    def get(self, search):
        data = searchBySubject(search)
        return data


api.add_resource(Index, '/')
api.add_resource(SeearchByCourse, '/course/<string:search>')
api.add_resource(SeearchBySubject, '/subject/<string:search>')

if __name__ == '__main__':
    app.run()
