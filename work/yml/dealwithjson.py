import json

key_list=["姓名","年龄","职业","工资"]
# def deal_with_dict(single_data):
#     for i in range(len(key_list)):
#         if len(single_data.get(key_list[i])) < 1:
#             single_data.get(key_list[i])=""

def read_json(filename):
    
    # the type of json_data is str
    json_data=open(filename,encoding='utf-8').read()
    # the type of data is list
    data=json.loads(json_data)
    for item in data:
        print(item)
        print(type(item))
        print(item.get('姓名',None))
    return data


if __name__ == '__main__':
    data = read_json('./test.json')