import boto3

ec2_client = boto3.client('ec2')
regions = [region['RegionName']
           for region in ec2_client.describe_regions()['Regions']]

for region in regions:
    ec2 = boto3.resource('ec2', region_name=region)
    print('Region {}: '.format(region))

    volumes = ec2.volumes.filter(
        Filters=[{'Name': 'status', 'Values': ['available']}])

    for volume in volumes:
        unattached_volume = ec2.Volume(volume.id)
        print('Deleting EBS volume: {}, Size: {} GiB'.format(unattached_volume.id, unattached_volume.size))
        unattached_volume.delete()