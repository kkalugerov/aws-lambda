import boto3

from datetime import datetime

# def lambda_handler(event, context):
ec2_client = boto3.client('ec2', region_name='us-east-1')
regions = [region['RegionName']
           for region in ec2_client.describe_regions()['Regions']]

for region in regions:
    print('Instances in EC2 Region {0}: '.format(region))
    ec2 = boto3.resource('ec2', region_name=region)

    instances = ec2.instances.filter(
        Filters=[
            {'Name': 'tag:backup', 'Values': ['true']}
        ]
    )

    timestamp = datetime.utcnow().replace(microsecond=0).isoformat()

    for instance in instances.all():
        for volume in instance.volumes.all():
            description = 'Backup of {0}, volume {1}, create {2}'.format(
                instance.id, volume.id, timestamp)
            print(description)

            snapshot = volume.create_snapshot(Description=description)

            print("Created snapshot: {}".format(snapshot.id))


# lambda_handler('', '')