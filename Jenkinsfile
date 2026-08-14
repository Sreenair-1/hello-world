pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Docker') {
            steps {
                bat 'echo PATH=%PATH%'
                bat 'where docker'
                bat 'dir "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe"'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'where docker'
                bat 'docker --version'
                bat 'docker info'
                bat 'docker build -t jenkins-demo-app:latest .'
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