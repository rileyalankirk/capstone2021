#!/bin/bash

cd ~/capstone2021
source .venv/bin/activate
git checkout remotes/origin/automate
python3 src/c21client/client.py
