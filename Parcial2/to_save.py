import requests
from datetime import date
import boto3

S3_BUCKET = 'headlines-ducuara'
s3 = boto3.client('s3')

#carga de archivos
def upload_file(file_name, bucket, object_name=None):
  if object_name is None:
    object_name = os.path.basename(file_name)
    try:
      response = s3.upload_file(file_name, bucket, object_name)
    except ClientError as e: 
      logging.error(e)
      return False
    return True   

url = "https://www.eltiempo.com"
name = "eltiempo"
fecha = date.today()
response = requests.get(url)
s3 = boto3.client('s3')
with open("/tmp/eltiempo.html",'wb+') as f:
    f.write(response.content)
    f.close()
with open("/tmp/eltiempo.html", "rb+") as f:
    s3.upload_fileobj(f, S3_BUCKET, f"raw/periodico={name}/year={fecha.year}/month={fecha.month}/day={fecha.day}/eltiempo-{fecha}.html")
    f.close()
