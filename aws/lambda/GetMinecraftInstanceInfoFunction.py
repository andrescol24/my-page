import boto3
import json
import os

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instance_id = os.environ.get('instance_id')
    instance_info = ec2.describe_instances(InstanceIds=[instance_id])
    current_state = instance_info['Reservations'][0]['Instances'][0]['State']['Name']
    if current_state == 'running':
        public_ip = instance_info['Reservations'][0]['Instances'][0]['PublicIpAddress']
        return build_http_response(200, {'running': True, 'ip': public_ip})
    else:
        return build_http_response(200, {'running': False, 'ip': None})
    
def build_http_response(code, body):
    return {
            'statusCode': code, 
            'headers': {
                "Content-Type": "application/json"
            },
            'body': json.dumps(body),
            'isBase64Encoded': False
        }
