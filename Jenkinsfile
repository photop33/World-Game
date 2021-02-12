pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                script {
                bat 'docker build -t 22 .'}
               }
            }
        stage('run') {
            steps {
                script {bat 'start/min docker run -p 8777:8080 22'}
               }
            }
        stage('e2e') {
            steps {
                script {bat 'python C:\\Users\\l1313\\.jenkins\\workspace\\Game-World\\e2e.py'}
            }
        }
        stage('stop') {
            steps {
                script {bat 'docker stop 22'}
            }
        }
    }
}
