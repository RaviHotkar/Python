## Install request module by running ->
#  pip3 install requests

# Replace the deviceToken key with the device Token for which you want to send push notification.
# Replace serverToken key with your serverKey from Firebase Console

# Run script by ->
# python3 fcm_python.py


import requests
import json
serverToken = 'AAAAsVRLRns:APA91bGv2pn57bNAcSLf6-9ntfiZXXCVC_x-BugGRl00Lb47YJYZCAq1SOjC_ZAoSX8y2RyMylc9xlgf1jsUkqTUf3CTpV59i2RSMp0rg9Ql25DtU5cRWxweFKwkYpswQE_qRHaqSMW7'
deviceToken = 'dvPpmRZfQN6IEouluY-UNH:APA91bGeCRNE4aQyzlgjnZqeDtm4tqMLI7oOkh-BCk-XXmQ9eiNG8bC1fHqo8la5crd7yn4CVeNVaR-qcYaeR8oL9JTZ-9VxgGLve0k0FF1ZGwjut8hU2MBzuYsw-5hAyTAidr_jyL1_'
## Read and replace deviceToken from token.txt file

headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
      }

body = {
          'notification': {'title': 'Replace with notification title',    
                            'body': 'Attach your response body'
                            },
          'to':
              deviceToken,
          'priority': 'high',
        #   'data': dataPayLoad,
        }
response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
print(response.status_code)
print(response.json())


