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

def csv_to_json(csv_file='example.csv', json_file='example.json'):
    json_list = []
    # with open('example.csv', newline='') as csvfile:
    with open(f'{csv_file}', newline='') as csvfile:
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
    with open(json_file) as jsonfile:
        json_dict=json.loads(jsonfile.read())
        print(json_dict[0])
        for key in json_dict[0]:
            print(f'{key},')
            keys.append(key)

        print(keys)


json_to_csv()
