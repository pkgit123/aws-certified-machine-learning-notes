# =================================================================
# Filename:       kinesis-put-record.py
# Description:    ACG course resource.
#                 Chapter 3:  Streaming Data Collection.
#                 Python app to generate streaming user data to Kinesis.
#                 Assume need to create Kinesis Stream beforehand?
# =================================================================

import requests
import boto3
import uuid
import time
import random
import json

# variables for boto3 Kinesis client
str_region_name = '<INSERT_YOUR_REGION>'
str_kinesis_stream_name = '<INSERT_YOUR_STREAM_NAME>'

# create unique identifier for partition, aka GUID
partition_key = str(uuid.uuid4())

# create Kinesis client in boto3
client = boto3.client('kinesis', region_name=str_region_name)

# generate user data, put into Kinesis Stream
while True:
    r = requests.get('https://randomuser.me/api/?exc=login')
    data = json.dumps(r.json())
    client.put_record(
        StreamName=str_kinesis_stream_name,
        Data=data
        PartitionKey=partition_key
    )
    time.sleep(random.uniform(0, 1))
