#!/bin/bash

scp -i ./ssh/id_rsa /home/jenkins/.jenkins/workspace/project2pipeline/docker-compose.yaml jenkins@35.247.113.36:docker-compose-stack.yaml
ssh -i ./ssh/id_rsa jenkins@35.247.113.36 << EOF
docker stack deploy --compose-file docker-compose-stack.yaml 
EOF
