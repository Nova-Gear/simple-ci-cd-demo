pipeline {
    agent any

    environment {
        SONARQUBE_ENV = "local-sonar"
        DOCKERHUB_CREDENTIALS = "dockerhub"
        IMAGE_NAME = "simple-ci-demo"
        DOCKERHUB_USER = "aljics4"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${env.SONARQUBE_ENV}") {
                    bat """
                        sonar-scanner ^
                        -Dsonar.projectKey=simple-ci-cd-demo ^
                        -Dsonar.sources=./app ^
                        -Dsonar.python.version=3.11 ^
                        -Dsonar.sourceEncoding=UTF-8
                    """
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 3, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat """
                        docker build -t %DOCKERHUB_USER%/%IMAGE_NAME%:latest .
                    """
                }
            }
        }

        stage('Push Docker') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: DOCKERHUB_CREDENTIALS,
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS'
                )]) {
                    bat """
                        docker login -u %USER% -p %PASS%
                        docker push %USER%/%IMAGE_NAME%:latest
                    """
                }
            }
        }
    }

    post {
        success {
            echo "CI Pipeline selesai: SonarQube PASS + Docker pushed."
        }
        failure {
            echo "Pipeline gagal!"
        }
    }
}
