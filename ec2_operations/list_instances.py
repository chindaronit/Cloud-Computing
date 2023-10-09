import boto3

# Create an EC2 resource object
ec2 = boto3.resource('ec2')

# Create an EC2 client
ec2_client = boto3.client('ec2')

# Create a filter for instances in various states
filters = [
    {
        'Name': 'instance-state-name', 
        'Values': ['running', 'stopped', 'pending', 'shutting-down', 'stopping']
    }
]

# Filter the instances based on the filters
instances = ec2.instances.filter(Filters=filters)


# Iterate through instances and print desired attributes
for instance in instances:
    # Print instance attributes
    print("Instance ID:", instance.id)
    print("Instance State:", instance.state['Name'])
    print("Instance Type:", instance.instance_type)
    print("Private IP Address:", instance.private_ip_address)
    print("Public IP Address:", instance.public_ip_address)
    print("Launch Time:", instance.launch_time)
    
    # Describe instance status
    instance_status = ec2_client.describe_instance_status(InstanceIds=[instance.id])
    
    # Check if status information is available
    if 'InstanceStatuses' in instance_status and instance_status['InstanceStatuses']:
        system_status = instance_status['InstanceStatuses'][0]['SystemStatus']['Status']
        instance_status = instance_status['InstanceStatuses'][0]['InstanceStatus']['Status']
        
        print("System Status:", system_status)
        print("Instance Status:", instance_status)
    else:
        print("Status information not available")
    
    print("\n\n")  # Print a new line for better readability
