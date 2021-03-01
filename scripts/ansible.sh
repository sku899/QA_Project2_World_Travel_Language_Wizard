#!/bin/bash
cd ~/.jenkins/workspace/project2pipeline
ansible-playbook -i inventory.yaml playbook.yaml 