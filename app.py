from data import getData, fetchSubjectCodes
from flask import Flask  # jsonify
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)
data = getData()


def containsSubjects(search, string):
    subjects = search.split('+')
    for i in subjects:
        if i.lower() not in string.lower():
            return False
    return True


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
            if containsSubjects(search, str(realData[course]))
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


class SeearchBySubjects(Resource):

    def get(self, search):
        data = searchBySubject(search)
        return data


class FetchSubjectCodes(Resource):

    def get(self):
        codes = fetchSubjectCodes()
        return codes


api.add_resource(Index, '/')
api.add_resource(SeearchByCourse, '/course/<string:search>')
api.add_resource(SeearchBySubject, '/subject/<string:search>')
api.add_resource(SeearchBySubjects, '/subjects/<string:search>')
api.add_resource(FetchSubjectCodes, '/codes/subjects')

if __name__ == '__main__':
    app.run()
