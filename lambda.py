import json
import base64
import gzip
import os
import requests

def lambda_handler(event, context):
    # TODO implement
    a = event["awslogs"]["data"]
    b = base64.b64decode(a)
    c = gzip.decompress(b)
    d = json.loads(c)
    e = d['logEvents'][0]['message']
    for i in range(len(e)):
        f = e.split(": ")[2]
        g = f.strip()
        headers = {
        'Accept': 'application/json',
        }
        data = {"game":"1", "team":"1", "order":g}
        response = requests.post('https://stats.aws.dev-null.link/proc/refund', headers=headers, data=data)
        print(response)
        print(data)
        print(len(e))


#1	Klayers-python38-requests	9	arn:aws:lambda:us-east-2:770693421928:layer:Klayers-python38-requests:9
