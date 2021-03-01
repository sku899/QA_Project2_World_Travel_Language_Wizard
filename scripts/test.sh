#!/bin/bash
pwd
echo 'here I am'
cd ./frontend
pip3 install -r requirements.txt
python3 -m pytest --cov app 
cd ..

cd ./backend
pip3 install -r requirements.txt
python3 -m pytest --cov app
cd ..

cd ./generator01
pip3 install -r requirements.txt
python3 -m pytest --cov app
cd ..

cd ./generator02
pip3 install -r requirements.txt
python3 -m pytest --cov app
cd ..
