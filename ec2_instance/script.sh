#cloud-boothook
#!/bin/bash
sudo yum install httpd -y
sudo service httpd start
sudo aws s3 sync s3://skywalkerlist/Website/ /var/www/html/
