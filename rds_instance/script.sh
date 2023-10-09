#!/bin/bash
mkdir portfolio
sudo aws s3 sync s3://skywalkerlist/data/ portfolio
cd portfolio
sudo yum install -y npm
sudo npm install
sudo node app.js
