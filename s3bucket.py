import boto3

s3_clientme=boto3.client("s3")

# list all buckets
response = s3_clientme.list_buckets()['Buckets']

# upload file
# response = s3_clientme.upload_file('/Users/admin/Documents/simplek8s/client-deployment.yaml','shubhamapril2023s3','client-deployment.yaml')

# download file
# response = s3_clientme.download_file('shubhamapril2023s3','first.py','first.py')

# create buket
# s3_clientme.create_bucket(Bucket="asalsknlasnalsnkasansa")

