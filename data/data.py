import json
# import os
# import sys

courses = open('data/jambitoMain.json')
subjects = open('data/subjectCodes.json')
schools = open('data/unis.json')

data = json.load(courses)
codeMap = json.load(subjects)
schools = json.load(schools)


def fetchSubjectCodes():
    return codeMap


def fetchSchools():
    schools["data"] = sorted(schools["data"])
    return schools


def getData():
    return data
