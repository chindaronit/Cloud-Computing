import boto3 

user_file = open("./user_script.sh", "r")
user_src = '\n'.join(user_file)

feedback_file = open("./feedback_script.sh", "r")
feedback_src = '\n'.join(feedback_file)

message_file = open("./message_script.sh", "r")
message_src = '\n'.join(message_file)


ec2=boto3.client('ec2')


def create_instance(type,server,src):
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
    InstanceId=instance['Instances'][0]['InstanceId']
    ec2_r = boto3.resource('ec2')
    instance=ec2_r.Instance(InstanceId)
    while(instance.state['Name']!='running'):
        instance=ec2_r.Instance(InstanceId)

    print(server + ' Server Created! ')
    print("endpoint : "+ ec2.describe_instances(InstanceIds=[InstanceId])['Reservations'][0]['Instances'][0]['PublicDnsName']) 

create_instance('t2.micro','User',user_src)
create_instance('t2.micro','Message',message_src)
create_instance('t2.micro','Feedback',feedback_src)




