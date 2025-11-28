pipeline {
    agent any

    environment {
        REGISTRY = "myregistry/myapp"
        IMAGE_TAG = "v${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Nova-Gear/simple-ci-cd-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat """
                docker build -t %REGISTRY%:%IMAGE_TAG% .
                """
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('my-sonar-server') {
                    bat "sonar-scanner"
                }
            }
        }

        stage('Docker Push') {
            steps {
                bat """
                docker push %REGISTRY%:%IMAGE_TAG%
                """
            }
        }

        stage('Update Helm Values & Push to Git (untuk ArgoCD)') {
            steps {
                powershell """
                Set-Content -Path deployment-image.txt -Value "image: $env:REGISTRY`:$env:IMAGE_TAG"
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
