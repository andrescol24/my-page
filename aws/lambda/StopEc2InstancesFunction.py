import boto3
import os
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=[os.environ.get('instance_id')])
    return {
        'statusCode': 200,
        'body': 'Stopped EC2 instance'
    }