from openpyxl import load_workbook
# from openpyxl.styles import PatternFill, Color
# from openpyxl.styles import NamedStyle

excel_file = 'jambito.xlsx'
workbook = load_workbook(excel_file, data_only=True)
olevel, uniCodes, jamb = list(workbook)

universities = {
    uniCodes[f'B{code}'].value: uniCodes[f'A{code}'].value
    for code in range(2, 166)
}


codeMap = {
    olevel[f'B{i}'].value: olevel[f'A{i}'].value
    for i in range(2, 28)
}


def getHex(cell):
    return cell.fill.start_color.index


def getSubjects(row):
    schoolInfo = []
    try:
        schoolInfo = [universities[cell.value]
                      for cell in row[15:] if cell.value is not None and
                      (cell.value != 'N/A' and cell.value != 'n/a')]
    except Exception:
        print(row[14])
    row = row[:14]
    hexes = set([getHex(cell) for cell in row if cell.value is not None])
    comp, ops, others = [], [], []
    for hx in hexes:
        if hx == '00000000' or hx == 'FFFFFFFF':
            comp.extend(
                [codeMap[cell.value] for cell in row if getHex(
                    cell) == hx and isinstance(cell.value, float)])
        else:
            subs = [codeMap[cell.value] for cell in row if getHex(
                cell) == hx and isinstance(cell.value, float)]
            if len(subs) > 1:
                ops.append(subs)
            else:
                others.append(subs)
    return {
        'subjects': {
            'compulsory': comp,
            'optional': {
                f'subject {i+1}': ops[i]
                for i in range(len(ops))
            },
            'others': others
        },
        'schools': schoolInfo
    }


def getData():
    data = {}

    for row in range(2, 663):
        data[jamb[f'O{row}'].value] = getSubjects(jamb[row])
    return {
        'results': data
    }


# import requests
# import json

# recipes = {
#   'results' : []
# }

# data = requests.get('http://127.0.0.1:5000/').json()

# print(data)
