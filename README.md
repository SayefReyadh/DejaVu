# DejaVu
A simple demo project which uploads the python files and csv files in a S3 bucket, later a lambda function is  triggered which reads the contents of the csv and upload it to a dynamodb table.

## Requirements

Run powershell as administrator to install software
1. Chocolatey: https://chocolatey.org/
2. Pycharm Professional: https://www.jetbrains.com/pycharm/download/
3. Python 3
  `choco install python3 -y`
4. NodeJS
  `choco install nodejs -y`
5. AWS CLI
  `choco install awscli -y`
6. Git
  `choco install git -y`
7. Pipenv
  `pip install pipenv`
8. Boto3
  `pip install boto3`
   
## AWS Console Configuration

#### [AWS IAM Console](https://console.aws.amazon.com/iam/home)
1. Navigate to the Users page.
2. Create an AWS IAM user whose credentials you're using.
3. Under the 'Permissions' section, attach the policy called 'AdministratorAccess '
4. Navigate to the Roles page.
5. Create a role.
6. Under the 'Permissions' section, attach the policy called 'AmazonS3FullAccess' 'AmazonDynamoDBFullAccess' 'AWSOpsWorksCloudWatchLogs' 


#### [Simple Storage Service (S3)](https://s3.console.aws.amazon.com/s3/home)
1. Create a Bucket with an unique bucket name.
2. Select Region `ap-south-1` [All S3 bucket is is Global]

#### [DynamoDB](https://ap-south-1.console.aws.amazon.com/dynamodb/home)
1. Select Region `ap-south-1` [DynamoDB Tables are Region Specific]
2. Create a table named `movies_characters` with primary key `actor_id` as  a  number. 

#### [Lambda](https://ap-south-1.console.aws.amazon.com/lambda/home)
1. Select Region `ap-south-1` [Lambda Functions are Region Specific]
2. Create a new lambda function with Author from scratch and named `csv-to-dynamodb` on runtime select `Python 3.8`, on execution role use the  existing role created back in IAM Roles.
3. Add trigger for our S3 Bucket, with Event type as `PUT` and Suffix as `.csv`
4. Upload the `lambda_function.py` file in the `csv-to-dynamodb` lambda.

## Basic Configuration

You need to set up your AWS security credentials before the code is able to connect to AWS. You can obtain the keys from the created IAM user's `Security Credentials`. 
Open up command prompt and write the following command `aws configure` 

    AWS Access Key ID : YOUR_KEY
    AWS Secret Access Key : YOUR_SECRET
    Default region name : ap-south-1
    Default output format : 

## Running the Project

This sample application connects to Amazon's S3
and uploads the python files and csv files in created bucket. Later the `csv-to-dynamodb` lambda is invoked and the contents of the csv files are uploaded in `movies_characters` dynamodb table. Change the `upload_file_bucket` variable of `dejavu.py` file with the S3 bucket name. 

    python dejavu.py
