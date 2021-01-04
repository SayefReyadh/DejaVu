import json
import csv
import boto3

def lambda_handler(event, context):
    
    region = 'ap-south-1'
    record_list = []
    try:
        s3 = boto3.client('s3')
        dynamodb = boto3.client('dynamodb' , region_name = region)
        
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        print('BUCKET: ' , bucket ,'KEY: ' , key)
        
        csv_file  = s3.get_object(Bucket = bucket , Key = key)
        
        record_list = csv_file['Body'].read().decode('utf-8').split('\n')
        csv_reader = csv.reader(record_list , delimiter = ',' , quotechar = '"')
        
        for row in csv_reader:
            actor_id = row[0]
            firstname = row[1]
            surname = row[2]
            salary = row[3]
            
                        print(actor_id , firstname , surname , salary)
            
            add_to_db = dynamodb.put_item(
                TableName = 'movies_characters',
                Item = {
                    'actor_id' : {'N': str(actor_id)},
                    'firstname' : {'S': str(firstname)},
                    'surname' : {'S': str(surname)},
                    'salary' : {'N': str(salary)},
                })
            
            print('Successfully added the records to the DyanamoDB Table')
        
    except Exception as e:
        print(str(e))
    
    return {
        'statusCode': 200,
        'body': json.dumps('CSV to  DynamoDB Success')
    }
