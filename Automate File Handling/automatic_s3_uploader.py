
import boto3
import os

client = boto3.client('s3')


for file in os.listdir():
    if '.py' in file:
        upload_file_bucket = 'dummy-bucket-sayefreyadh' #A dummy s3 bucket
        upload_file_key = 'python/' + str(file) #A sub dir to store py files
        client.upload_file(file , upload_file_bucket, upload_file_key)
