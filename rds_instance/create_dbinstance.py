import boto3 
import time

rds=boto3.client('rds')


response = rds.create_db_instance(
    DBName='portfolio',
    DBInstanceIdentifier='skywalker-db',
    DBInstanceClass='db.t3.micro',
    Engine='MySQL',
    EngineVersion= "8.0",
    MasterUsername='victus',
    MasterUserPassword="victus123",
    VpcSecurityGroupIds=[
       'sg-0512f6fe1c3f33655'
    ],
    AllocatedStorage=20,
    AvailabilityZone='ap-south-1a',
    DBSubnetGroupName='default-vpc-0a62c737f4bad4838',
    Port=3306,
    PubliclyAccessible=True,
)

i=0
while True:
    try:
        # Retrieve the RDS endpoint
        response=response = rds.describe_db_instances(
            DBInstanceIdentifier='skywalker-db',
        )
        
        rds_endpoint = response['DBInstances'][0]['Endpoint']['Address']
        print("endpoint : "+str(rds_endpoint))
        break
    except:
        print(f"Trying to get endpoint ({i})")
        i +=1
        time.sleep(7)
        






