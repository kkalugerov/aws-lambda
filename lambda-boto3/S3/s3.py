import boto3

s3 = boto3.resource('s3')

# for bucket in s3.buckets.all():
bucket = s3.Object(bucket_name='tf-remote-state-bucket-2k19',key='experimental')
print(bucket.bucket_name)
print(bucket.key)