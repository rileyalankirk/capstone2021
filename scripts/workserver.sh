#!/bin/bash

cd /home/vagrant/capstone2021
source .venv/bin/activate
sudo git checkout remotes/origin/automate
sudo python3 src/c21server/work_server/work_server.py
