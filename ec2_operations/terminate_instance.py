import boto3

# Create an EC2 resource object
ec2 = boto3.resource('ec2')

# Create an EC2 client
ec2_client = boto3.client('ec2')

# Create a filter for instances in the running state
filters = [
    {
        'Name': 'instance-state-name', 
        'Values': ['running','stopped',"stopping"]
    }
]

# Filter the instances based on the filters
instances = ec2.instances.filter(Filters=filters)

# terminate instances
for instance in instances:
    response = ec2_client.terminate_instances(
        InstanceIds=[
            instance.id,
        ],
    )

    print(response)
    print("\n")