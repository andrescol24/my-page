import boto3
import json
import os

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    body = json.loads(event["body"])
    if is_valid_user(body):
        result = start_instance_if_not_running(os.environ.get('instance_id'))
        if result['statusCode'] == 200:
            print(f"{body.get('user')} has started the server")
        return result
    else:
        return {'statusCode': 403}

def is_valid_user(body):
    password = os.environ.get(body.get('user'), None)
    if password:
        return body.get('password') == password
    return False

def start_instance_if_not_running(instance_id):
    instance_info = ec2.describe_instances(InstanceIds=[instance_id])
    current_state = instance_info['Reservations'][0]['Instances'][0]['State']['Name']
    if current_state == 'running':
        return build_http_response(206, {'message': 'El servidor ya esta corriendo'})
    elif current_state == 'stopped':
        return start_instance_and_write_ip(instance_id)
    else:
        return build_http_response(406, {'message': f"No puedes iniciar el servidor porque tiene el estado de: {current_state}."})

def start_instance_and_write_ip(instance_id):
    ec2.start_instances(InstanceIds=[instance_id])
    waiter = ec2.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])
    instance_info = ec2.describe_instances(InstanceIds=[instance_id])
    public_ip = instance_info['Reservations'][0]['Instances'][0]['PublicIpAddress']
    write_ip(public_ip)
    return build_http_response(200, {'running': True, 'ip': public_ip})

def write_ip(public_ip):
    s3_body = """{{"running": true, "ip": "{0}"}}""".format(public_ip)
    s3.put_object(Bucket=os.environ.get('s3_bucket'), Key='server_status.json', Body=s3_body)

def build_http_response(code, body):
    return {
            'statusCode': code, 
            'headers': {

                "Content-Type": "application/json"
            },
            'body': json.dumps(body),
            'isBase64Encoded': False
        }