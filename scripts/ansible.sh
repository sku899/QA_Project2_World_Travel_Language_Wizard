#!/bin/bash
cd ansible_project2
ansible-playbook -i inventory.yaml playbook.yaml
cd ..
