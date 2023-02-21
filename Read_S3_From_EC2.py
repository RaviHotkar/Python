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


print(client)

s3 = boto3.resource('s3')
bucket = s3.Bucket('fala-app-images')


obj = s3.Object(bucket_name=bucket, key='PWDS.txt')
print(obj.bucket_name)
print(obj.key)

response = obj.get()
data = response['Body'].read()

print(s3)
print(bucket)

#client.object = client.Bucket('https://fala-app-images.s3.ap-south-1.amazonaws.com/').Object('PWDS.txt').get()

#path = client.bucket('s3://fala-app-images').object('PWDS.txt').get()


#print(path)

'''
model='arn:aws:rekognition:ap-south-1:453183322705:project/Tomato_V1/version/Tomato_V1.2022-11-02T12.45.46/1667373573682'
bucket = "custom-labels-console-ap-south-1-034b3ae05d"
photo  = "Test_images/11 (2).JPG"

serverToken = 'AAAAsVRLRns:APA91bGv2pn57bNAcSLf6-9ntfiZXXCVC_x-BugGRl00Lb47YJYZCAq1SOjC_ZAoSX8y2RyMylc9xlgf1jsUkqTUf3CTpV59i2RSMp0rg9Ql25DtU5cRWxweFKwkYpswQE_qRHaqSMW7'
deviceToken = 'dvPpmRZfQN6IEouluY-UNH:APA91bGeCRNE4aQyzlgjnZqeDtm4tqMLI7oOkh-BCk-XXmQ9eiNG8bC1fHqo8la5crd7yn4CVeNVaR-qcYaeR8oL9JTZ-9VxgGLve0k0FF1ZGwjut8hU2MBzuYsw-5hAyTAidr_jyL1_'
## Read and replace deviceToken from token.txt file

'''

#s3 = boto3.resource('s3')

#print('S3 location is read...')
#print(s3)

#s3.object = s3.Bucket('https://fala-app-images.s3.ap-south-1.amazonaws.com/').Object('PWDS.txt').get()


#print('actual bucket loaded...')
#print(s3.object)

#https://fala-app-images.s3.ap-south-1.amazonaws.com/

'''



def lambda_handler(event, context):
    response = "**********************************************Hello FaLa****************************************** "
    print(response)
    client = boto3.client("rekognition")
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    
    print("bucket_name")
    print(bucket_name)
    
    key = event['Records'][0]['s3']['object']['key']
    key = urllib.parse.unquote_plus(key,encoding='utf-8')
    
    print("------------- > File to be analyzed = ")
    print(key)
    
    #print("event")
    #print(event)
    #print("context")
    #print(context)
    #s3 = boto3.client("s3")
    #response = client.detect_labels(Image={"S3Object": {"Bucket": "custom-labels-console-ap-south-1-034b3ae05d", "Name": "Test_images/11 (1).JPG"}},MaxLabels=3,MinConfidence=80)
    #response = client.detect_labels(Image={'S3Object':{"Bucket":"custom-labels-console-ap-south-1-034b3ae05d","Name":"Test_images/11 (1).JPG"}},"MaxLabels":10,"MinConfidence":75)
    
    photo = key
    
    #response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},MaxLabels=3,MinConfidence=90)
    response = client.detect_custom_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},MinConfidence=30,ProjectVersionArn=model)  #'I am bringing message from AWS Lambda' #
    print(response)
    
    
    
    #-----Akshay code begin----
    
        body = {
          'notification': {'title': 'Replace with notification title',    
                            'body':  json.dumps(response)   #response  #
                            },
          'to':
              deviceToken,
          'priority': 'high',
        #   'data': dataPayLoad,
        }
    
    encoded_body = json.dumps({
        'notification': {'title': 'Hello',    
                         'body':  json.dumps(response)   #response
                            },
          'to':
              deviceToken,
          'priority': 'high',
        #   'data': dataPayLoad,
    })

    http = urllib3.PoolManager()

    response_post_gfb = http.request('POST', 'https://fcm.googleapis.com/fcm/send',
                 headers={'Content-Type': 'application/json', 'Authorization': 'key=' + serverToken,},
                 body=encoded_body)
    
    
    
    
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
      }
    

    
  #  http = urllib3.PoolManager()
  #  r = http.request('POST', 'http://httpbin.org/robots.txt')
    
    #response_post_gfb = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
    print(response_post_gfb.status_code)
    print(response_post_gfb.json())
    
    #-----Akshay code end----
    
    response_temp = "**********************************************END of test****************************************** "
    print(response_temp)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
'''