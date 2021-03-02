#!/bin/bash

ssh -i ~/.ssh/id_rsa rsku888@35.247.113.36 << EOF
cd ~/World_Travel_Language_Wizard/
sudo docker stack deploy --compose-file docker-compose-stack.yaml
EOF
