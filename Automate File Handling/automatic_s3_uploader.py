
import boto3
import os

client = boto3.client('s3')

upload_file_bucket = 'csv-dynamo-lambda-sayefreyadh'  # A dummy s3 bucket

for file in os.listdir():
    if '.py' in file:
        upload_file_key = 'python/' + str(file)  # A sub dir to store py files
        client.upload_file(file, upload_file_bucket, upload_file_key)

    elif '.csv' in file:
        upload_file_key = str(file)
        client.upload_file(file , upload_file_bucket, upload_file_key)
