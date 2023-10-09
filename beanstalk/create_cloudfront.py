import boto3


client = boto3.client("cloudfront")

response = client.create_distribution(
    DistributionConfig={
        "CallerReference": "skywalkerdistribution",
        "DefaultRootObject": "index.html",
        "Origins": {
            "Quantity": 1,
            "Items": [
                {
                    "Id": "skywalkercloudfrontid",
                    "DomainName": "skywalkerlist.s3.ap-south-1.amazonaws.com",
                    "S3OriginConfig": {"OriginAccessIdentity": ""},
                },
            ],
        },
        
        'DefaultCacheBehavior': dict(
                TargetOriginId = 'skywalkercloudfrontid',
                ViewerProtocolPolicy= 'redirect-to-https',
                TrustedSigners = dict(Quantity=0, Enabled=False),
                ForwardedValues=dict(
                    Cookies = {'Forward':'all'},
                    Headers = dict(Quantity=0),
                    QueryString=False,
                    QueryStringCacheKeys= dict(Quantity=0),
                    ),
                MinTTL=1000
        ),
        "Comment": "distribution to host portfolio",
        "Enabled": True,
    }
)

print(response)
