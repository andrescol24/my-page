import time
import os
import boto3
import logging
from datetime import datetime
from mcstatus import JavaServer

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

LAMBDA_FUNCTION_NAME = "StopEc2InstancesFunction"
MINECRAFT_SERVER_IP = "localhost"
MINECRAFT_SERVER_PORT = 25565
LAST_EMPTY_TIME_FILE = '/tmp/cron_verify_server.txt'

def check_minecraft_server():
    try:
        server = JavaServer.lookup(f"{MINECRAFT_SERVER_IP}:{MINECRAFT_SERVER_PORT}")
        status = server.status()
        return status.players.online
    except Exception as e:
        print(f"Error checking Minecraft server status: {e}")
        return None

def trigger_lambda_shutdown():
    lambda_client = boto3.client('lambda', region_name='us-east-1')
    try:
        response = lambda_client.invoke(
            FunctionName=LAMBDA_FUNCTION_NAME,
            InvocationType='Event'
        )
        print(f"Lambda function invoked: {response}")
    except Exception as e:
        print(f"Error invoking Lambda function: {e}")

def read_last_empty_time():
    if os.path.exists(LAST_EMPTY_TIME_FILE):
        with open(LAST_EMPTY_TIME_FILE, 'r') as file:
            content = file.read()
            if content == '':
                return None
            else:
                return float(content)
    return None

def write_last_empty_time(timestamp):
    with open(LAST_EMPTY_TIME_FILE, 'w+') as file:
        file.write(str(timestamp))

# Main logic
def main():
    last_empty_time = read_last_empty_time()
    player_count = check_minecraft_server()
    if player_count is not None:
        logging.info(f"Running validation, players: {player_count}")
        if player_count == 0:
            if last_empty_time is None:
                last_empty_time = time.time()
                write_last_empty_time(last_empty_time)
            elif time.time() - last_empty_time >= 300:  # 5 minutes = 300 seconds
                logging.info("Server has been empty for 5 minutes, triggering shutdown.")
                trigger_lambda_shutdown()
                last_empty_time = None
                write_last_empty_time('')
        else:
            last_empty_time = None
            write_last_empty_time('')

if __name__ == "__main__":
    main()
