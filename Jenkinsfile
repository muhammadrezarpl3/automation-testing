pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
             steps {
                  bat 'python -m pytest -v --junitxml=test-results.xml --html=pytest-report.html --self-contained-html'
                }
            }
        }
        post {
             always {
                junit 'test-results.xml'
             }
        }
}