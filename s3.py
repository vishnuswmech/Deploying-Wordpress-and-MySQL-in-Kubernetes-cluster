import boto3
import config
s3 = boto3.client("s3", 
                  region_name='us-east-1', 
                  aws_access_key_id= config.access_key, 
                  aws_secret_access_key= config.secret_key)

bucket_response = s3.list_buckets()
buckets = bucket_response["Buckets"]

for i in buckets:
    print(i)

