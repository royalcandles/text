import csv
import json

# with open('example.csv', newline='') as csv_file:
#     reader = csv.DictReader(csv_file)
#     data = [row for row in reader]
#
#     # 将 Python 字典列表转换为 JSON 字符串
# json_data = json.dumps(data)
#
# # 将 JSON 字符串写入文件
# with open('example.json', 'w') as json_file:
#     json_file.write(json_data)
import sys


def csv_to_json(csv_file='example.csv', json_file='example.json'):
    json_list = []
    # with open('example.csv', newline='') as csvfile:
    with open(f'{csv_file}', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            json_list.append(row)

    json_data = json.dumps(json_list, indent=2)
    # 将 JSON 字符串写入文件
    with open(f'{json_file}', 'w') as jsonfile:
        jsonfile.write(json_data)


def json_to_csv(csv_file='example.csv', json_file='example.json'):
    # json_list = []
    keys = []
    with open(json_file, 'r', newline='') as jsonfile:
        json_dict = json.loads(jsonfile.read())
        # 打开json文件，获取表头。
        print(json_dict[0])
        for key in json_dict[0]:
            keys.append(key)
    with open(csv_file, 'w', newline='') as csvfile:
        print(keys)
        # 在csvfile文件以keys为表头，依次写入相应数据。
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(json_dict)


def get_file(input_type, input_file):
    if input_type == '-b':
        csv_file_name = str(input_file)
        csv_to_json(csv_flie_name, f'{csv_file_name[0:-3]}' + '.py')
    elif input_type == '-p':
        json_file_name = str(input_file)
        json_to_csv(json_file_name, f'{json_file_name[0:-2]}' + ".csv")


get_file(sys.argv[1], sys.argv[2])
