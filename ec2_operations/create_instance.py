import boto3

file = open("./script.sh", "r")

src = '\n'.join(file)
ec2 = boto3.client('ec2')

def check_status(instance): 
    InstanceId=instance['Instances'][0]['InstanceId']
    ec2_r = boto3.resource('ec2')
    instance=ec2_r.Instance(InstanceId)
    while(instance.state['Name']!='running'):
        instance=ec2_r.Instance(InstanceId)

    print(ec2.describe_instances(InstanceIds=[InstanceId])['Reservations'][0]['Instances'][0]['PublicDnsName'])


def create_instance(type):
    instance = ec2.run_instances(
        ImageId='ami-0ded8326293d3201b',
        InstanceType=type,
        MaxCount=1,
        MinCount=1,
        KeyName='skywalker_key',
        SecurityGroups=['launch-wizard-2'],
        IamInstanceProfile={
            'Name': 'ec2S3connector'
        },
        UserData=src
    )    
    check_status(instance)


create_instance('t2.micro')
create_instance('t2.nano')
create_instance('t2.nano')