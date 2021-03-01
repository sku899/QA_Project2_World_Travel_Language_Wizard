#!/bin/bash
pwd

cd ./frontend
pip3 install -r requirements.txt
python3 -m pytest --cov app 
cd ..

cd ./backend
python3 -m pytest --cov app
cd ..

cd ./generator01
python3 -m pytest --cov app
cd ..

cd ./generator02
python3 -m pytest --cov app
cd ..