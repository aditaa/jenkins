#!/bin/bash

yum install -y java-1.7.0-openjdk git python-argparse
wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo
rpm --import http://pkg.jenkins-ci.org/redhat-stable/jenkins-ci.org.key
yum install -y jenkins
git config --global user.name "jenkins ig2ad"
git config --global user.email jenkins@ig2ad.com
yum -y update & >> /tmp/update.log
wget https://region-a.geo-1.objects.hpcloudsvc.com/v1/27696061931890/jenkins/Backup-Current.tar.gz -O /tmp/Backup-Current.tar.gz
cd /tmp
tar -xf Backup-Current.tar.gz
cd /tmp/Backup
mv * /var/lib/jenkins/
service jenkins start/stop/restart
chkconfig jenkins on