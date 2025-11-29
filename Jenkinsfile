pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Nova-Gear/simple-ci-cd-demo.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('my-sonar-server') {
                    bat "sonar-scanner"
                }
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
