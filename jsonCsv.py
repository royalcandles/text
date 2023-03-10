import json
import csv

data_2 = [
    {
        "name": "Alice",
        "age": 25,
        "gender": "female",
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345"
        },
        "phoneNumbers": [
            {
                "type": "home",
                "number": "555-1234"
            },
            {
                "type": "work",
                "number": "555-5678"
            }
        ]
    },
    {
        "name": "Bob",
        "age": 30,
        "gender": "male",
        "address": {
            "street": "456 Oak St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345"
        },
        "phoneNumbers": [
            {
                "type": "home",
                "number": "555-9876"
            },
            {
                "type": "work",
                "number": "555-4321"
            }
        ]
    }
]
print(type(data_2))
json_str2 = json.dumps(data_2, indent=2)

# print(json_str2)
# print(type(json_str2))

keys = []
for key in data_2[0]:
    print(f'{key},')
    keys.append(key)

print(keys)

with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = keys
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 写入表头
    writer.writeheader()

    # 写入多行数据
    writer.writerows(data_2)