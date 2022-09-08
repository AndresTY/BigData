import json
import boto3
import function

S3_BUCKET = 'dolar-raw-ducuara'
s3 = boto3.client('s3')
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
    object_key = "dolar-timestamp.txt"
    file_content = s3.get_object(Bucket=S3_BUCKET, Key=object_key)["Body"].read()
    with open('/tmp/data_raw.csv','w+') as f:
      f.write(function.data_to_csv(file_content))
      f.close()
    with open("/tmp/data_raw.csv", "rb") as f:
      s3.upload_fileobj(f, "dolar-processed-ducuara", "dolar-timestamp.csv")
    return {'statusCode': 200,'body': 'check'}
