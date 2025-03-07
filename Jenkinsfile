pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/CosmoJelly/mlops-assignment1.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cosmojelly/mlops-assignment1:latest .'
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
                    sh 'docker push cosmojelly/mlops-assignment1:latest'
                }
            }
        }
    }
    post {
        success {
            sh 'echo "Deployment Successful" | mail -s "Jenkins Deployment Notification" admin@example.com'
        }
    }
}

