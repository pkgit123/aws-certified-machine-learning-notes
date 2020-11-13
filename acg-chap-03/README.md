# Chapter 3 Streaming Data Collection

There is a Stream Data Collection lab at the end of the chapter.  

### Steps: 
1. AWS Console -> Kinesis -> Create Data Stream
    * Use region US-east-1
    * Give the stream a name
    * Estimate the number of shards 
    * Use AWS shard calculator based on record size and number per second
1. AWS Console -> CloudFormation -> Create stack
    * Use region US-east-1
    * Upload template
    * CloudFormation template to spin up EC2 and other resources
    * Give the stack a name
    * Requires Kinesis stream name
    * Allow CloudFormation to create IAM role
    * The CloudFormation template includes code from the Python app, starts producing data
1. AWS Console -> Kinesis -> click on existing stream
    * Click on the "Monitoring" tab -> PutRecords API call
    * Monitoring every 1 minute
1. AWS Console -> Kinesis -> Create Analytics Application
    * Give the application a name and description
    * Choose runtime: SQL or Apache Flink
    * Click button for "Connect Streaming Data"
    * Choose Kinesis Stream or Kinesis Firehose delivery system
    * Other options and configurations
    * Allow it to create/update IAM role
    * Click button for "Discover Schema" -> see raw vs. formatted format
    * Save and continue
1. AWS Console -> Kinesis -> Realtime Analytics -> Go to SQL Editor
    * Write realtime SQL query
    * Create stream "DESTINATION_USER_DATA"
    * Create pump "STREAM_PUMP"
    * Select stream, SQL select query.  
    * In Kinesis Data Analytics, SOURCE_SQL_STREAM_001 is by default the main stream from the source. In this case, it’s receiving the source payload from Kinesis Data Streams.  See reference link below.
    * Click on destination -> Connect to a Destination: (a) Kinesis Stream, (b) Kinesis Firehose, (c) AWS Lambda
    * Destination -> Choose Kinesis Firehose -> Create new delivery stream -> Source "DirectPUT"
    * Use AWS Lambda under "Record Transformation" to add new line after records -> Choose Lambda blueprint -> General Firehose Processing
    * Choose Lambda function created in next step
1. AWS Lambda console
    * Function name: add-newline-function
    * Create new IAM role with lambda 
    * Default is NodeJS code -> Create Function
    * Edit the function code using file
    * The Kinesis Firehose data is encoded in base64
    * Increase Lambda timeout to 1 minute
    * Save lambda
    * Go back to previous step, select this Lambda
1. AWS Console -> Kinesis -> Firehose
    * Choose Lambda function created in next step
    * Option to convert json to Apache Parquet or Apache ORC -> requires AWS Glue
    * Destination: (a) S3, (b) Redshift, (c) Amazon Elastic Search, (d) Splunk
    * Choose S3 as destination: bucket name and prefix
    * Choose S3 buffer conditions: buffer size (1MB) and buffer interval (60 seconds)
    * Allow IAM to create role for Kinesis Firehose to have access to S3 bucket
1. AWS Console -> Kinesis -> Realtime Analytics
    * Choose Kinesis Firehose Delivery Stream
    * Choose in-application stream name: "DESTINATION_USER_DATA"
    * Create IAM role
    * Save and continue
1. AWS Console -> S3 -> bucket
    * see user data refresh


### Files:
1. kinesis-put-record.py - Python application to retrieve user data using API, and put records into a Kinesis Data Stream.
1. setup-data-producer.yml - CloudFormation template to spinup EC2 and other resources, to create Kinesis data producer
1. create-subset-transformation-query.sql - SQL query string for Kinesis Realtime Analytics, for transformation.
1. lambda-index.js - NodeJS lambda code to add newline after records in Kinesis Firehose output


### Reference:
1. https://aws.amazon.com/blogs/big-data/create-real-time-clickstream-sessions-and-run-analytics-with-amazon-kinesis-data-analytics-aws-glue-and-amazon-athena/
    * In Kinesis Data Analytics, SOURCE_SQL_STREAM_001 is by default the main stream from the source. In this case, it’s receiving the source payload from Kinesis Data Streams.
