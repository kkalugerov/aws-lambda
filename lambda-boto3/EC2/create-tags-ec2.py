import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
reservations =   ec2.describe_instances(
    Filters=[{'Name': 'instance-state-name',
              'Values': ['running']}])["Reservations"]
tags = [{
    "Key" : "backup",
       "Value" : "true"
    },
    {
       "Key" : "Name",
       "Value" : "boto3-ec2"
    }]

for reservation in reservations :
    for each_instance in reservation["Instances"]:
        ec2.create_tags(
            Resources = [each_instance["InstanceId"] ],
            Tags= tags
           )