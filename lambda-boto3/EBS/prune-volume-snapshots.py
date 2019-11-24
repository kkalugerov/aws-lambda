import boto3

account_id = boto3.client('sts').get_caller_identity().get('Account')
ec2_client = boto3.client('ec2', region_name='us-east-1')
regions = [region['RegionName']
           for region in ec2_client.describe_regions()['Regions']]

for region in regions:
    print('Instances in EC2 Region {}: '.format(region))
    ec2 = boto3.client('ec2', region_name=region)

    response = ec2.describe_snapshots(OwnerIds=[account_id])
    snapshots = response['Snapshots']

    # Sort snapshots by date ascending
    snapshots.sort(key=lambda x: x['StartTime'])
    print("Current Snapshots: {}".format(snapshots))

    # Remove all snapshots except the 3 most recent
    snapshots = snapshots[:-3]

    for snapshot in snapshots:
        id = snapshot['SnapshotId']
        try:
            print("Deleting snapshot: {}".format(id))
            ec2.describe_snapshots(SnapshotId=id)
        except Exception as ex:
            if 'InvalidSnapshot.InUse' in ex.message:
                print('Snapshot {} in use, skipping.'.format(id))
