import csv
from collections import defaultdict
# for date manipulation, use the below:
# from datetime import datetime, timedelta
# from dateutil.relativedelta import relativedelta


# encoding for CSV files created in Windows is windows-1250
def importFile(filename, fileMode, fileEnc):
    with open(filename, fileMode, encoding=fileEnc) as f:
        reader = csv.DictReader(f)
        data = list(reader)
        return data


def exportFileList(data, filename, fileMode):
    with open(filename, fileMode) as export:
        wr = csv.writer(export, delimiter=',')
        wr.writerows([x.split(',') for x in data])


def exportFileLOL(data, filename, fileMode):
    with open(filename, fileMode) as export:
        wr = csv.writer(export, delimiter=',')
        wr.writerows(data)


def findID(data, field_name):
    for entry in data:
        if entry['FULL_NAME'] == field_name:
            return entry['STAFF_ID']
    return field_name


def groupData(data, key_name):
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data


def trimValues(data, key_name, value_name):
    trimmed_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        value = data_point[value_name]
        trimmed_data[key] = float(value)
    return trimmed_data


def countGroupedItems(grouped_data, field_name):
    count_data = {}

    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += 1
        count_data[key] = total

    return count_data


def sumGroupedItems(grouped_data, field_name):
    summed_data = {}

    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        summed_data[key] = total

    return summed_data


def getValue(staff_id, table_name, column_name):
    for entry in table_name:
        if entry['STAFF_ID'] == staff_id:
            result = entry[column_name]
            return result
    return 'n/a'
