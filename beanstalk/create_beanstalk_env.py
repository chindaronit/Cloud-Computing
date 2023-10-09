import boto3

client = boto3.client("elasticbeanstalk")


client.create_application_version(
    ApplicationName="victus_app",
    AutoCreateApplication=True,
    Description="chinda_ronit portfolio website",
    Process=True,
    SourceBundle={
        "S3Bucket": "skywalkerlist",
        "S3Key": "Portfolio.zip",
    },
    VersionLabel="v1",
)

import time

while True:

    response = client.describe_application_versions(
        ApplicationName="victus_app",
        VersionLabels=[
            "v1",
        ],
        MaxRecords=1,
    )

    if response["ApplicationVersions"][0]["Status"] != "PROCESSED":
        print("Trying to create Application...")
        time.sleep(5)
    else:
        print("Succesfully created Application...")
        break
    

response = client.create_environment(
    ApplicationName="victus_app",
    CNAMEPrefix="skywalker",
    EnvironmentName="victus-env",
    SolutionStackName="64bit Amazon Linux 2 v5.8.5 running Node.js 18",
    VersionLabel="v1",
    OptionSettings=[
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "IamInstanceProfile",
            "Value": "ec2S3connector",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "InstanceType",
            "Value": "t2.micro",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "EC2KeyName",
            "Value": "skywalker_key",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "ImageId",
            "Value": "ami-097e7acc1d0c8b1b9",
        },
        {
            "Namespace": "aws:autoscaling:launchconfiguration",
            "OptionName": "SecurityGroups",
            "Value": "sg-0512f6fe1c3f33655",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Statistic",
            "Value": "Average",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "Period",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "UpperThreshold",
            "Value": "80",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "UpperBreachScaleIncrement",
            "Value": "1",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "MeasureName",
            "Value": "CPUUtilization",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "LowerThreshold",
            "Value": "20",
        },
        {
            "Namespace": "aws:autoscaling:trigger",
            "OptionName": "LowerBreachScaleIncrement",
            "Value": "-1",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "Availability Zones",
            "Value": "Any 2",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "MaxSize",
            "Value": "3",
        },
        {
            "Namespace": "aws:autoscaling:asg",
            "OptionName": "MinSize",
            "Value": "1",
        },
        {
            "Namespace": "aws:ec2:vpc",
            "OptionName": "Subnets",
            "Value": "subnet-0fa516ae7d97502fa"
        },

    ],
)

print("Envoirnment Created...")