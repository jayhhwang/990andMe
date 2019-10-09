import json
import pandas as pd
import sys
import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('YEAR')

#Collect indices by year
indexListing = pd.read_json(r'INDICES_BY_YEAR.json')
addresses = []
for i in range(0, len(indexListing)):
    current = indexListing.iloc[i][0]
    address = current['URL'][38:]
    addresses.append(address)

#Copy files in year to new S3 bucket
def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3.Object(bucket_to_name, file_name).copy(copy_source)

for index, item in enumerate(addresses):
    try:
        copy_to_bucket(bucket_to_name, bucket_to_name, file_name)
        print('%s out of %s successfully copied.' % (index, len(addresses)))
    except:
        print('%s out of %s not successful' % (index, len(addresses)))
