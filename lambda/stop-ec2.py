import boto3

# def lambda_handler(event, context):
ec2_client = boto3.client('ec2', region_name='us-east-1')
regions = [region['RegionName']
            for region in ec2_client.describe_regions()['Regions']]

for region in regions:
    ec2 = boto3.resource('ec2', region_name=region)

    print("Region: ", region)

    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name',
                  'Values': ['running']}])
                  # 'Values': ['stopped']}])

    for instance in instances:
        # instance.stop()
        instance.terminate()
        print('Stopped instance: ', instance.id)

# lambda_handler()