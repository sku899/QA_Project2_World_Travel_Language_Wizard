pipeline {
    agent any
    environment {
        DOCKERHUB_LOGIN = credentials("DOCKERHUB_LOGIN")
    }
    stages {
        stage('Test'){
            steps{
                sh 'chmod +x ./scripts/test.sh'
                sh './scripts/test.sh'
            }
        }
        stage('Build and Push'){
            steps{
                sh 'chmod +x ./scripts/buildandpush.sh'
                sh './scripts/buildandpush.sh'
            }
        }
        stage('Ansible'){
            steps{
                sh 'chmod +x ./scripts/ansible.sh'
                sh './scripts/ansible.sh'
            }
        }
        stage('Deploy'){
            steps{
                sh 'chmod +x ./scripts/deploy.sh'
                sh './scripts/deploy.sh'
            }
        }                   
    }
}
