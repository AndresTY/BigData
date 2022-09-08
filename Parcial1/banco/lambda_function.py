import json
import urllib3
import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_file(file_name, bucket, object_name=None):
  if object_name is None:
    object_name = os.path.basename(file_name)
    s3_client = boto3.client('s3')
  try:
    response = s3_client.upload_file(file_name, bucket, object_name)
  except ClientError as e:
    logging.error(e)
    return False
  return True

def lambda_handler(event, context):
  http = urllib3.PoolManager()
  data =  http.request('GET', 'https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario')
  print(str(data.data,'utf-8'), file=open('/tmp/dolar-timestamp.txt', 'w+'))
  s3 = boto3.client('s3')
  with open("/tmp/dolar-timestamp.txt", "rb") as f:
    s3.upload_fileobj(f, "dolar-raw-ducuara", "dolar-timestamp.txt")
  return {'statusCode': 200,
          'body': data.data}  
