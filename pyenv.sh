#!/bin/bash

sudo yum install -y  gcc gcc-c++ make git patch openssl-devel zlib-devel readline-devel sqlite-devel bzip2-devel

git clone git://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PATH="~/.pyenv/bin:${PATH}"' >> .bashrc
#echo 'eval "$(pyenv init -)"' >> .bashrc
source ~/.bashrc

pyenv install 3.7.0
pyenv install 2.7.0

#sudo yum update -y
sudo yum install -y python3-pip
sudo  pip install virtualenv
sudo yum install -y python-virtualenv

exec $SHELL