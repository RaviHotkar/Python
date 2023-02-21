from secrets import access_key , secret_access_key
import json
import boto3
import urllib.parse
#from botocore.vendored import requests
import urllib3
import os

client = boto3.client('s3',
                     aws_access_key_id = access_key,
                     aws_secret_access_key = secret_access_key )
                     
print('All set to start...')

response = client.get_object(Bucket = 'fala-app-images' , Key = 'Latest_location.txt')

#print(response)

data = response['Body'].read()

print(data)

#s3://fala-app-images/JSW006/token.txt