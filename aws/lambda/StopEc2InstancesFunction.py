import boto3
import os

s3 = boto3.client('s3')
ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=[os.environ.get('instance_id')])
    clean_s3_information()
    return {
        'statusCode': 200,
        'body': 'Stopped EC2 instance'
    }

def clean_s3_information():
    s3_body = "{\"running\": false, \"ip\": null}"
    s3.put_object(Bucket=os.environ.get('s3_bucket'), Key='server_status.json', Body=s3_body)