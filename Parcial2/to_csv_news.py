from bs4 import BeautifulSoup
import boto3
import time
import json
from datetime import date

#configuracion del bucket
S3_BUCKET = 'headlines-ducuara'
s3 = boto3.client('s3')

def to_csv(file):
    file_content = s3.get_object(Bucket=S3_BUCKET, Key=file)["Body"].read() #obtencion del archivo
    soup = BeautifulSoup(file_content, "html.parser")
    text = "tema|id|tema|link|structure\n"
    for articles in soup.find_all('article'):
        for links in articles.find_all('a'): 
            try:
                link = links["href"]
                tema = link.split('/')[1]
                id_news = links["id"]
                code = soup.select_one(f"a#{id_news}").get_text(strip=True, separator=" ")
                text += f"{code}|{id_news}|{tema}|{link}|{links}\n"
            except:
                ...
    return text
    
name = "eltiempo"
fecha = date.today()
object_key = f"raw/periodico={name}/year={fecha.year}/month={fecha.month}/day={fecha.day}/eltiempo-{fecha}.html" #objeto a llamar


with open('/tmp/data_news.csv','wb+') as f:
    f.write(to_csv(object_key).encode('utf-8')) #escritura de los datos transformados
    f.close()
with open("/tmp/data_news.csv", "rb+") as f:
    s3.upload_fileobj(f, "headlines-ducuara", f"final/periodico={name}/year={fecha.year}/month={fecha.month}/day={fecha.day}/eltiempo-{fecha}.csv") #carge archivo CSV
