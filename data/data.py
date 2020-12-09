import json

courses = open('data\\jambitoMain.json',)
subjects = open('data\\subjectCodes.json',)

data = json.load(courses)
codeMap = json.load(subjects)


def fetchSubjectCodes():
    return codeMap


def getData():
    print('right here boss')

    # for row in range(2, 663):
    #     data[jamb[f'O{row}'].value] = getSubjects(jamb[row])
    return {
        'results': data
    }
