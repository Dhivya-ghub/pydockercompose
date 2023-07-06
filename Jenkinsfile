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
        stage('Docker Testing') {
          steps {
                sh 'wget 34.219.56.142:5001'
            }
        }
        stage('DockerHub login') {
          steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
              
               }
           }
        
        stage('Run Docker push') {
          steps {
                sh 'docker push dhivyadhub/pythonapp:1 && docker push dhivyadhub/pythonapp:'
                }
           }    
    }
}    

