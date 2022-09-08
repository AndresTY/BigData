import json

def data_to_csv(data):
    info = ""
    data = json.loads(data)
    for i in data:
        info += str(i[0]) + '\t' + str(i[1]) + '\n'
    return info
