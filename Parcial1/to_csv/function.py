import json
import time
from datetime import datetime

def data_to_csv(data):
    info =""
    data = json.loads(data)
    for i in data:
        info += i[0] +'\t'+str(datetime.utcfromtimestamp(int(i[0])/1000).strftime('%Y-%m-%d %H:%M:%S'))+'\t'+ i[1]+'\n'
        
    return info
