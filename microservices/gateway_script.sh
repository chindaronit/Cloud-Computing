#!/bin/bash
sudo mkdir gateway
sudo aws s3 sync s3://skywalkerlist/gateway/ gateway
cd gateway
sudo yum install -y docker
sudo service docker start
sudo docker build -t gateway .
sudo docker run -p 80:8001 -t user