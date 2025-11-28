pipeline {
    agent any

    environment {
        REGISTRY = "myregistry/myapp"
        IMAGE_TAG = "v${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YOUR_USERNAME/simple-ci-cd-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t $REGISTRY:$IMAGE_TAG .
                """
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('my-sonar-server') {
                    sh "sonar-scanner"
                }
            }
        }

        stage('Docker Push') {
            steps {
                sh """
                docker push $REGISTRY:$IMAGE_TAG
                """
            }
        }

        stage('Update Helm Values & Push to Git (untuk ArgoCD)') {
            steps {
                sh """
                echo "image: $REGISTRY:$IMAGE_TAG" > deployment-image.txt
                """
            }
        }
    }

    post {
        success {
            echo "Pipeline success!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
