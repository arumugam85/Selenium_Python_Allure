# import openpyxl
#
#
# def readData():
#         list = []
#         # path = "C:\\Users\\Arumugam\\PycharmProjects\\ECommerce_Demo\\InputData.xlsx"
#         path = ".//TestData/InputData.xlsx"
#         workbook = openpyxl.load_workbook(path)
#         sheet = workbook["addcust"]
#
#         rows = sheet.max_row
#         cols = sheet.max_column
#
#         for r in range(2, rows + 1):
#             email = sheet.cell(r, 1).value
#             password = sheet.cell(r, 2).value
#             firstname = sheet.cell(r, 3).value
#             lastname = sheet.cell(r, 4).value
#             gender = sheet.cell(r, 5).value
#             dob = sheet.cell(r, 6).value
#             company = sheet.cell(r, 7).value
#             newsletter = sheet.cell(r, 8).value
#             role = sheet.cell(r, 9).value
#             vendor = sheet.cell(r, 10).value
#             comment = sheet.cell(r, 11).value
#
#             tuple = (email, password, firstname, lastname, gender, dob, company, newsletter, role, vendor, comment)
#             list.append(tuple)
#             return list
