import os
import json
import csv
import sys


# 将JSON文件转换为CSV文件
def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)

    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(json_data.keys())
        writer.writerow(json_data.values())


# 将CSV文件转换为JSON文件
def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        data = next(reader)

    json_data = dict(zip(header, data))

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False)


def get_file(input_type, input_file):
    if str(input_type) == '-b':
        csv_file = str(input_file)
        output_file = os.path.splitext(csv_file)[0] + '.json'
        csv_to_json(csv_file, output_file)
    elif str(input_type) == '-p':
        json_file = str(input_file)
        output_file = os.path.splitext(json_file)[0] + '.csv'
        json_to_csv(json_file, output_file)


get_file(sys.argv[1], sys.argv[2])
