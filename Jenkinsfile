pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                script {
                bat 'docker build -t 20 .'}
               }
            }
        stage('run') {
            steps {
                script {bat ' docker run -p 8777:8080 20'}
               }
            }
        stage('e2e') {
            steps {
                script {bat 'python C:\\Users\\l1313\\.jenkins\\workspace\\Game-World\\e2e.py'}
            }
        }
        
    }
}
