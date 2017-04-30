# coding=utf-8
import xlrd

def genSourceData(file):
    wBook = xlrd.open_workbook(file)
    sheetName = wBook.sheet_names()[0]
    sheet = wBook.sheet_by_name(sheetName)
    interfaceList = []

    nrows = sheet.nrows
    ncols = sheet.ncols

    curRow = 1
    for i in range(1, nrows):
        if str(sheet.cell(i, 0)).strip() != '':
            # print str(sheet.cell(i,0)).rsplit(":")[1]
            print sheet.cell(i,0).value

    return interfaceList

if __name__ == "__main__":
    fileName = "C:\\Users\\zuohaitao\\Desktop\\HTTPTest\\HTTPTest\\interfaceData.xlsx"
    print genSourceData(fileName)



