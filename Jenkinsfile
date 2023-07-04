node {
     checkout scm 
     environment {
        docker_repo = "dhivyadhub/pydocker1"
        DOCKERHUB_CREDENTIALS = credentials('dockerHub')
     } 
    stage ('Cleaning Local Images and Containers') {
                 sh 'docker stop $(docker ps -a -q) || true && docker rm $(docker ps -a -q) || true && docker rmi -f $(docker images -a -q) || true'
     }
    stage('docker-compose build ') {
                 sh 'docker-compose build && docker-compose up -d'
    }
    stage('docker containers testing') {
                 sh 'wget 18.236.253.227:5001' 
    }   
    stage('docker images  push') {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push dhivyadhub/pythonapp:1 && docker push dhivyadhub/sqlapp:1'
               
    }     
}
