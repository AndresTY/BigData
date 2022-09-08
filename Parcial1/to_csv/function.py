import json

#convert responde in csv
def data_to_csv(data):
    info = ""
    data = json.loads(data) #load string as json
    for i in data:
        info += str(i[0]) + '\t' + str(i[1]) + '\n' #csv format
    return info
