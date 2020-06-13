from openpyxl import load_workbook
# from openpyxl.styles import PatternFill, Color
# from openpyxl.styles import NamedStyle

excel_file = 'jambito.xlsx'
workbook = load_workbook(excel_file, data_only=True)
worksheets = workbook.get_sheet_names()
jamb, olevel = workbook[worksheets[1]], workbook[worksheets[0]]


def getHex(cell):
    return cell.fill.start_color.index


codeMap = {olevel[f'B{i}'].value: olevel[f'A{i}'].value for i in range(2, 28)}


def getSubjects(row):
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
        'compulsory': comp,
        'optional': {
            f'subject {i+1}': ops[i]
            for i in range(len(ops))
        },
        'others': others
    }


def getData():
    data = {}

    for row in range(2, 665):
        data[jamb[f'O{row}'].value] = getSubjects(jamb[row])
    return {
        'results': data
    }
