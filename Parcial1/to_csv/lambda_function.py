#Importaciones
import json
import boto3
import function
import time

#configuracion del bucket
S3_BUCKET = 'dolar-raw-ducuara'
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

def lambda_handler(event, context):
  object_key = "dolar-timestamp.txt" #objeto a llamar
  file_content = s3.get_object(Bucket=S3_BUCKET, Key=object_key)["Body"].read() #obtencion del archivo
  with open('/tmp/data_raw.csv','w+') as f:
    f.write(function.data_to_csv(file_content)) #escritura de los datos transformados
    f.close()
  with open("/tmp/data_raw.csv", "rb") as f:
    s3.upload_fileobj(f, "dolar-processed-ducuara", f"dolar-{time.time()}.csv") #caarge archivo CSV
  return {'statusCode': 200,'body': 'check'}
