pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t jenkins-demo-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker rm -f jenkins-demo-app || exit 0'
                bat 'docker run -d -p 5000:5000 --name jenkins-demo-app jenkins-demo-app'
            }
        }

        stage('Test') {
            steps {
                bat 'curl http://localhost:5000'
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }
        failure {
            echo 'CI/CD Pipeline failed!'
        }
    }
}