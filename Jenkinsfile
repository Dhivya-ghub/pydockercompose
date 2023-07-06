pipeline {
    agent any
    environment {
        docker_repo = "dhivyadhub/pythonapp"
        DOCKERHUB_CREDENTIALS = credentials('dockerHub')
    } 
    stages {
        stage ('Cleaning Local Images and Containers') {
           steps {
               sh 'docker stop $(docker ps -a -q) || true && docker rm $(docker ps -a -q) || true && docker rmi -f $(docker images -a -q) || true'
           }
        }
        stage('Docker Build') {
           steps {
                sh 'docker-compose build'
            }  
        }
        stage('Run Docker container') {
          steps {
                sh 'docker-compose up -d'
            }
        }
       
    }
}    

