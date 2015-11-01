import xlrd


def build_json_from_row(row, iterator):
    sub_json = {}
    next_row = iterator.next()
    if next_row[2] == "":
        return row[5], next_row

def build_json():
    json_artifact = {}
    row_iterator = get_worksheet_row()
    row = row_iterator.next()
    json_artifact[row[1]], next_row = build_json_from_row(row, row_iterator)
    print json_artifact

def main():
    build_json()


def get_worksheet_row():
    workbook = xlrd.open_workbook('data_confidential/Department of Agriculture and Cooperation.xls')
    worksheet = workbook.sheets()[0]
    for row_num in range(11, worksheet.nrows):
        yield worksheet.row_values(row_num)


#
main()


# {
#     "Secretariat - Economic Services": "81.93",
#     "Krishonnati Yojana (Central) - Crop Husbandry" : {
#         "Seeds":{
#             "Development and strengthening of seed infrastructure facilities for production and distribution of Seeds": "224.23",
#             "Sub-Mission on Seeds and Planting Material": "0",
#             "Other Programmes": "17.46",
#             "total" : "241.69"
#         }
#     }
# }