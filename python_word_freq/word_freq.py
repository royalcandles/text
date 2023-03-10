import json
import sys


def output(obj):
    print(json.dumps(obj))


file = sys.argv[1]
with open(f'{file}', 'r', encoding='utf-8') as f:
    data = f.read()
    # 将所有的标点符号舍去。
    translation_table = str.maketrans('!,.?\n', '     ')
    data_list = data.translate(translation_table)
    # 将所有的词放在列表里保存。
    data_list = data_list.split(' ')
    data_dict = {}
    for i in data_list:
        if i not in data_dict.keys():
            data_dict[i] = 1
        else:
            data_dict[i] += 1
    # 删除字典中的空字符value。
    del data_dict['']
    output(data_dict)
