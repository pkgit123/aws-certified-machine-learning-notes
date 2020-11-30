# https://github.com/ACloudGuru-Resources/Course_AWS_Certified_Machine_Learning/blob/master/Chapter5/box-plot-example.ipynb
# !python --version

import boto3
import pandas as pd
from sagemaker import get_execution_role
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

role = get_execution_role()
bucket='<YOUR_BUCKET_NAME_HERE>'
data_key = 'car_data.csv'
data_location = 's3://{}/{}'.format(bucket, data_key)
print(data_location)

df = pd.read_csv(data_location)

df.head()

df_vet = df[df['car'] == 'Corvette']
df_mustang = df[df['car'] == 'Mustang']
df_camaro = df[df['car'] == 'Camaro']

data = [df_camaro['engine_hp'], df_vet['engine_hp'], df_mustang['engine_hp']]
plt.boxplot(data, vert=False)
plt.title('Engine HP Box Plot')
plt.xlabel('Engine HP')
plt.yticks([1, 2, 3], ['Camaro', 'Corvette', 'Mustang'])
plt.show()
