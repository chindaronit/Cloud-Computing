#!/bin/bash
sudo mkdir message
sudo aws s3 sync s3://skywalkerlist/message/ message
cd message
sudo yum install -y docker
sudo service docker start
sudo docker build -t message .
sudo docker run -p 80:8002 -t message

