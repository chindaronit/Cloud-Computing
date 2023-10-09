#!/bin/bash
sudo mkdir feedback
sudo aws s3 sync s3://skywalkerlist/feedback/ feedback
cd feedback
sudo yum install -y docker
sudo service docker start
sudo docker build -t feedback .
sudo docker run -p 80:8003 -t feedback