pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t jenkins-demo-app:latest .'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker rm -f test-container || true

                    docker run -d \
                        --name test-container \
                        --network jenkins-network \
                        jenkins-demo-app:latest

                    sleep 5

                    curl -f http://test-container:5000/test

                    docker rm -f test-container
                '''
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