import json
import boto3

s3_client=boto3.client('s3')
dyno=boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket_name='16may2023shubham'
    file_name='mydata.json'
    
    json_obj=s3_client.get_object(Bucket=bucket_name,Key=file_name)
    json_read=json_obj['Body'].read()
    json_dict=json.loads(json_read)
    
    for line in json_dict:
        table=dyno.Table('mytable')
        table.put_item(Item=line)
    return 'Hello' 
    