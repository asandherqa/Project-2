pipeline {
    agent any
    environment {
        DATABASE_URI = credentials('DATABASE_URI')
    }
    stages {
        stage('Configure environment') {
            steps{
                sh "cat ansible-playbook.yaml"
                sh "~/.local/bin/ansible-playbook -i inventory.yaml ansible-playbook.yaml"
            }
        }
        stage('Build Images'){
            steps{
                sh "sudo docker-compose up -d --build"
            }
        }
        stage('Test'){
            steps{
                sh "cd ./server && pytest --cov=app --cov-report html"
                sh "cd ./class_api && pytest --cov=app --cov-report html"
                sh "cd ./prize_api && pytest --cov=app --cov-report html"
                sh "cd ./ticket_api && pytest --cov=app --cov-report html"
            }
        }
        stage('Push Containers'){
            steps {
            sh "sudo docker-compose push"
            }
        }
        stage('Pull to swarm'){
            steps {
            sh "scp ${workspace}/docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml"
            sh "ssh jenkins@swarm-manager 'docker stack deploy --compose-file docker-compose.yaml pryze"
            }
        }
    }
}