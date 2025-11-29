pipeline {
    agent any

    tools {
        sonarQubeScanner "sonar-scanner"
    }

    environment {
        SONARQUBE_ENV = "local-sonar"
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
                        -Dsonar.projectName=simple-ci-cd-demo ^
                        -Dsonar.sources=./app ^
                        -Dsonar.language=py ^
                        -Dsonar.sourceEncoding=UTF-8
                    """
                }
            }
        }

        stage("Quality Gate") {
            steps {
                timeout(time: 10, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline selesai, SonarQube PASS"
        }
        failure {
            echo "Pipeline gagal!"
        }
    }
}
