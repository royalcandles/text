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


# # 测试代码
if __name__ == '__main__':
    file_type = sys.argv[1]
    file_name = sys.argv[2]
    if file_name == '-b':
        csv_to_json(f'{file_name}', f'{file_name[0:-3]}+json')
    elif file_type == '-p':
        json_to_csv(f'{file_name}', f'{file_name[0:-4]}+csv')
