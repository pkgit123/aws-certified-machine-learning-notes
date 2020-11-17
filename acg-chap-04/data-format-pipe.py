# =============================================================================================================
# ACloudGuru Certified Machine Learning Chapter 4.6 - Other Feature Engineering
# See example of data format file vs. pipe
# See also https://towardsdatascience.com/machine-learning-on-aws-sagemaker-b23e32503106 Written by Mahsa Mir
# =============================================================================================================
'''
References: 
 * https://data.solita.fi/machine-learning-building-blocks-in-aws-sagemaker/
 * https://towardsdatascience.com/machine-learning-on-aws-sagemaker-b23e32503106 
 * https://pypi.org/project/sagemaker-experiments/
'''


# =============================================================================================================
# Code version ACloudGuru CML Chapter 4.6
# =============================================================================================================

from sagemaker.amazon.common import write_numpy_to_dense_tensor
import io
import boto3

bucket = 'bucket-name' # use the name of your s3 bucket here
data_key = 'kmeans_lowlevel_example/data'
data_location = f's3://{bucket}/{data_key}'

# convert training data into format for algorithm
buf = io.Bytes.IO()
write_numpy_to_dense_tensor(buf, train_set[0], train_set[1])
buf.seek(0)

# location to upload to recordIO-protobuf data
boto3.resource('s3').Bucket(bucket).Object(data_key).upload_fileobj(buf)



# =============================================================================================================
# Code version Mahsa Mir https://towardsdatascience.com/machine-learning-on-aws-sagemaker-b23e32503106 
# =============================================================================================================

#import module in terms of dealing with various types of I/O
import io

#import sagemaker common library
import sagemaker.amazon.common as smac 

#converts the data in numpy array format to RecordIO format
buf = io.BytesIO()
smac.write_numpy_to_dense_tensor(buf, X_train, y_train)

#reset in-memory byte arrays to zero
buf.seek(0)

#import module
import os
 
#Key refers to the name of the file    
key = 'linear-train-data'
#uploads the data in record-io format to S3 bucket
boto3.resource('s3').Bucket(bucket).Object(os.path.join(prefix, 'train', key)).upload_fileobj(buf)

#training data location in s3
s3_train_data = 's3://{}/{}/train/{}'.format(bucket, prefix, key)print('uploaded training data location: {}'.format(s3_train_data))

