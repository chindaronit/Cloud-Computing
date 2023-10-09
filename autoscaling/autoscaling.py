import boto3
import base64

file = open("./script.sh", "r")
src = '\n'.join(file)
ec2 = boto3.client('ec2')
autoscaling_client = boto3.client('autoscaling')
cloudwatch = boto3.client('cloudwatch')
encoded_src = base64.b64encode(src.encode()).decode('utf-8')


# defining some values for further use 
GroupName="skywalker_group"
TemplateName="skywalker_scaler"
KeyName='skywalker_key'
SecurityGroupIds=['sg-0512f6fe1c3f33655']
InstanceType="t2.micro"
UserData=encoded_src
IamInstanceProfile='ec2S3connector'
minSize=1
maxSize=3


# for launching template
def launch_template(TemplateName,InstanceType,UserData,KeyName,SecurityGroup,IamInstacneProfile):
    template = ec2.create_launch_template(
        LaunchTemplateName=TemplateName,
        LaunchTemplateData={
            'ImageId': 'ami-0ded8326293d3201b',  
            'InstanceType': InstanceType,
            'SecurityGroupIds': SecurityGroup,
            'KeyName':KeyName,
            'UserData': UserData,
            'IamInstanceProfile':{
                'Name': IamInstacneProfile
            },
        }
    )
    return template

# for creating autoscaling group
def create_autoscaling_group(TemplateName,GroupName,minSize,maxSize):
    autoscaling_group = autoscaling_client.create_auto_scaling_group(
        AutoScalingGroupName=GroupName,
        LaunchTemplate={
            'LaunchTemplateName': TemplateName,
            'Version': '$Default',
        },
        MinSize=minSize,
        MaxSize=maxSize,
        DesiredCapacity=2,
        VPCZoneIdentifier='subnet-0fa516ae7d97502fa',  
    )
    return autoscaling_group

# for creating scaling policy
scale_in_policy = {
    'PolicyName': 'scale_in',
    'AutoScalingGroupName': GroupName,
    'AdjustmentType': 'ChangeInCapacity',
    'PolicyType': 'StepScaling',
    'StepAdjustments': [
        {
            'MetricIntervalUpperBound':0,
            'ScalingAdjustment': -1,          
        },
    ],
    'Cooldown': 300,
}
    
scale_out_policy= {
    'PolicyName': 'scale_out',
    'AutoScalingGroupName': GroupName,
    'AdjustmentType': 'ChangeInCapacity',
    'PolicyType': 'StepScaling',
    'StepAdjustments': [
        {
            'MetricIntervalLowerBound': 0, 
            'ScalingAdjustment': 1,          
        },
    ],
    'Cooldown': 300,
}


template=launch_template(TemplateName,InstanceType,UserData,KeyName,SecurityGroupIds,IamInstanceProfile)
print(template)
autoscaling_group=create_autoscaling_group(TemplateName,GroupName,minSize,maxSize)
print(autoscaling_group)

scale_in_policy_response = autoscaling_client.put_scaling_policy(**scale_in_policy)
scale_out_policy_response= autoscaling_client.put_scaling_policy(**scale_out_policy)

print(scale_in_policy_response)
print(scale_out_policy_response)


# create alarms 
scale_out_alarm={
    'AlarmName': 'HighUtilization',
    'ComparisonOperator': 'GreaterThanOrEqualToThreshold',
    'EvaluationPeriods': 1,
    'MetricName': 'CPUUtilization',
    'Namespace': 'AWS/EC2',
    'Period': 60,
    'Statistic': 'Average',
    'Threshold': 50,
    'AlarmDescription': 'Alarm when server CPU exceeds 80%',
    'AlarmActions': [scale_out_policy_response['PolicyARN']],
    'Dimensions' : [
        {
            'Name' : 'AutoScalingGroupName',
            'Value' : 'skywalker_group'
        }
    ]
}

scale_in_alarm={
    'AlarmName': 'LowUtilization',
    'ComparisonOperator': 'LessThanOrEqualToThreshold',
    'EvaluationPeriods': 1,
    'MetricName': 'CPUUtilization',
    'Namespace': 'AWS/EC2',
    'Period': 60,
    'Statistic': 'Average',
    'Threshold': 20,
    'AlarmDescription': 'Alarm when server CPU falls short of 20%',
    'AlarmActions': [scale_in_policy_response['PolicyARN']],
    'Dimensions' : [
        {
            'Name' : 'AutoScalingGroupName',
            'Value' : 'skywalker_group'
        }
    ]
    
}

cloudwatch.put_metric_alarm(**scale_in_alarm)
cloudwatch.put_metric_alarm(**scale_out_alarm)


# Filter for running instances
filters = [
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
]

# # Retrieve information about the running instances
response = ec2.describe_instances(Filters=filters)

# Iterate through the reservationsec2-3-109-108-140.ap-south-1.compute.amazonaws.com to get instance information
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        # Check if the instance has a public DNS name
        if 'PublicDnsName' in instance:
            instance_id = instance['InstanceId']
            public_dns_name = instance['PublicDnsName']
            print(f"Instance ID: {instance_id}, Public DNS Name: {public_dns_name}")
        else:
            instance_id = instance['InstanceId']
            print(f"Instance ID: {instance_id}, Public DNS Name: N/A (No Public DNS Name)")
