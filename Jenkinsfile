pipeline {
    agent any
    stages {
        stage('build docker ') {
            steps {
                script {
                dockerImage = docker.build "world-game" + ":$BUILD_NUMBER"  
		bat 'echo docker number success'
                 }
               }
            }
        stage('set version') { 	
            steps {	
                bat "echo IMAGE_TAG=${BUILD_NUMBER} > .env"   
	        bat "more .env"
                bat "echo secsses  ${BUILD_NUMBER}"
	    }
               }
	stage('run') {
            steps {
                script {
			
                    bat 'docker run -p 8777:8777  "world-game:'$BUILD_NUMBER'"'
                    bat 'echo docker run'
                 }
               }
            }
        stage('build dockerdocker ompose ') {
            steps {
                script {
                bat "docker-compose up -d"
                bat 'echo docker-compose up success'
                 }
               }
            }
        stage('e2e') {
            steps {
                script {
                    bat 'python C:\\Users\\l1313\\.jenkins\\workspace\\Game-World\\e2e.py'
                    bat 'echo e2e.py'
                 }
               }
            }
        stage('Test') {  
            steps {  
                bat 'echo "Fail!"; exit 1'  
                 }
               }
            }
      post {  
            always {  
                echo 'This will always run'  
            }  
            success {  
                echo 'This will run only if successful'  
            }  
            failure {  
                mail bcc: '', body: "<b>Example</b><br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', subject: "ERROR CI: Project name -> ${env.JOB_NAME}", to: "foo@foomail.com";  
            }  
            unstable {  
                echo 'This will run only if the run was marked as unstable'  
            }  
            changed {  
                echo 'This will run only if the state of the Pipeline has changed'  
                echo 'For example, if the Pipeline was previously failing but is now successful'  
            }  
        }
    }
