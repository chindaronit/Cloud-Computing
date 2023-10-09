#!/bin/bash
sudo mkdir user
sudo aws s3 sync s3://skywalkerlist/user/ user
cd user
sudo yum install -y docker
sudo service docker start
sudo docker build -t user .
sudo docker run -p 80:8001 -t user 