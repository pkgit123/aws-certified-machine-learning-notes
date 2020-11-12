# =================================================================
# Filename:       kinesis-put-record.py
# Description:    ACG course resource.
#                 Chapter 3:  Streaming Data Collection.
#                 Python app to generate streaming user data to Kinesis.
#                 Assume need to create Kinesis Stream beforehand?
# =================================================================
'''
https://github.com/ACloudGuru-Resources/Course_AWS_Certified_Machine_Learning/blob/master/Chapter3/put-record-python-program.py
'''

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

# Added 08/2020 since randomuser.me is starting to throttle API calls
# The following code loads 500 random users into memory
number_of_results = 500
r = requests.get('https://randomuser.me/api/?exc=login&results=' + str(number_of_results))
data = r.json()["results"]

# generate user data, put into Kinesis Stream
while True:
    # The following chooses a random user from the 500 random users pulled from the API in a single API call.
    random_user_index = int(random.uniform(0, (number_of_results - 1)))
    random_user = json.dumps(data[random_user_index])
    client.put_record(
        StreamName=str_kinesis_stream_name,
        Data=random_user
        PartitionKey=partition_key
    )
    time.sleep(random.uniform(0, 1))
