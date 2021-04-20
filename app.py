from data.data import getData, fetchSubjectCodes, fetchSchools
from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)
api = Api(app)
data = getData()


def containsSubjects(search, string):
    codes = fetchSubjectCodes()
    subjects = search.split('+')
    for i in subjects:
        if not re.search(codes[i].lower(), string.lower()):
            return False
    return True


def searchByCourse(search):
    data, search = getData(), search.upper()
    realData = data['results']
    courses = realData
    return {
        'results': {
            course: realData[course]
            for course in courses
            if search in course
        }
    }


def searchBySubject(search):
    print(search)
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


class FetchSubjectCodes(Resource):

    def get(self):
        codes = fetchSubjectCodes()
        return codes


class FetchSchools(Resource):

    def get(self):
        schools = fetchSchools()
        return schools


api.add_resource(Index, '/')
api.add_resource(SeearchByCourse, '/course/<string:search>')
api.add_resource(SeearchBySubject, '/subjects/<string:search>')
api.add_resource(FetchSubjectCodes, '/codes/subjects')
api.add_resource(FetchSchools, '/schools')

if __name__ == '__main__':
    app.run()
