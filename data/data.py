import json
import os
import sys

courses = open('data/jambitoMain.json')
subjects = open(os.path.join(sys.path[0], 'data/subjectCodes.json'),)

data = json.load(courses)
codeMap = json.load(subjects)


def fetchSubjectCodes():
    return codeMap


def getData():
    # print('right here boss')

    return {
        'results': data
    }
