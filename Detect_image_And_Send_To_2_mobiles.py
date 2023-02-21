import json
import boto3
import urllib.parse

#from botocore.vendored import requests
import urllib3

#model='arn:aws:rekognition:ap-south-1:453183322705:project/Tomato_V1/version/Tomato_V1.2022-11-02T12.45.46/1667373573682'
model='arn:aws:rekognition:ap-south-1:908288426135:project/Fala_ver1_reko/version/Fala_ver1_reko.2022-11-08T12.41.34/1667891728171'
bucket = "custom-labels-console-ap-south-1-719d8963bb"
photo  = "Test_Images/Broccoli___Alternaria_leaf_spot (1).jpg"

serverToken = 'AAAAsVRLRns:APA91bGv2pn57bNAcSLf6-9ntfiZXXCVC_x-BugGRl00Lb47YJYZCAq1SOjC_ZAoSX8y2RyMylc9xlgf1jsUkqTUf3CTpV59i2RSMp0rg9Ql25DtU5cRWxweFKwkYpswQE_qRHaqSMW7'
deviceToken1 = 'cwjon4BmQlGsqkpTMCWkzP:APA91bGNXeCIhnB2h9VLY4SL_UjHSttNpdyfVbZUeVmBdkN5A0LeCPNQp4-qNAkkpLJ58ys05t2b03tx2lOerE12-Ue-by9JeQFK6GkhFAEP6K7oSc-hGbG_s_vNyaryXXrmx7aEEZpx'
deviceToken2 = 'c1IZmyHEQY6dwv62Dp1nGD:APA91bHXh85c-RElhtec_QRRu1SAEqyqIdZCx_u5TKLmBoG45-IhUIeBITm6n_TN0IChaZjfi-BYqX0x2OlqXPbsZguG1_gj7oqiWmpiVnp7VI-VYShTYEcuFxk5S_PQufTp3TPWLr4C'
## Read and replace deviceToken from token.txt file

def lambda_handler(event, context):
    response = "**********************************************Hello FaLa****************************************** "
    print(response)
    

    
    client = boto3.client("rekognition")
    
   # print("---------------------------------> Starting the model <--------------------------------------")
   # response=client.start_project_version(ProjectVersionArn=model, MinInferenceUnits=1)
    print(response)
    
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
    response = client.detect_custom_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},MinConfidence=30,ProjectVersionArn=model)
    print(response)
   

   # print("---------------------------------> Stopping the model <--------------------------------------")
    #response=client.stop_project_version(ProjectVersionArn=model)
    print(response)
    
    response_string =response['CustomLabels']
    print('response_string ==============')
    print(response_string)
    
    #-----Akshay code begin----

    encoded_body = json.dumps({
        'notification': {'title': 'Message From FaLa App',    
                         'body':  json.dumps(response_string)   #response
                            },
          'to':
              deviceToken1,
          'priority': 'high',
        #   'data': dataPayLoad,
    })

    http = urllib3.PoolManager()

    response_post_gfb = http.request('POST', 'https://fcm.googleapis.com/fcm/send',
                 headers={'Content-Type': 'application/json', 'Authorization': 'key=' + serverToken,},
                 body=encoded_body)
                 
                 
    encoded_body1 = json.dumps({
        'notification': {'title': 'Hello',    
                         'body':  json.dumps(response_string)   #response
                            },
          'to':
              deviceToken2,
          'priority': 'high',
        #   'data': dataPayLoad,
    })

    http = urllib3.PoolManager()

    response_post_gfb = http.request('POST', 'https://fcm.googleapis.com/fcm/send',
                 headers={'Content-Type': 'application/json', 'Authorization': 'key=' + serverToken,},
                 body=encoded_body1)
    
    



    
    #response_post_gfb = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
    print(response_post_gfb.status_code)
    print(response_post_gfb.json())
    
    #-----Akshay code end----
    
    
    


    response = "**********************************************END of test****************************************** "
    print(response)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
