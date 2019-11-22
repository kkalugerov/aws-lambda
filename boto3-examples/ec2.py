import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')
response = ec2.run_instances(
	ImageId='ami-04763b3055de4860b',
	InstanceType='t2.micro',
	# KeyName='boto3-examples-ec2',
	MinCount=1,
	MaxCount=1
)

print(response)
