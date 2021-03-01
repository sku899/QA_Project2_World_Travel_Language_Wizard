#!/bin/bash

#scp -i ./ssh/id_rsa /home/jenkins/.jenkins/workspace/project2pipeline/docker-compose-stack.yaml jenkins@35.247.113.36:docker-compose-stack.yaml
sudo ssh -i ./ssh/id_rsa jenkins@35.247.113.36 << EOF
## ssh -i ~/.ssh/jenkins_agent_key swarmanager << EOF
#docker stack deploy --prune --with-registry-auth --resolve-image=always --compose-file docker-compose-stack.yaml
sudo rm -rf World_Travel_Language_Wizard
git clone https://github.com/sabinaku/World_Travel_Language_Wizard.git
cd World_Travel_Language_Wizard
sudo docker stack deploy --compose-file docker-compose-stack.yaml myapp
EOF
