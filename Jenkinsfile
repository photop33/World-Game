pipeline {
    agent any
    environment { 
        registry = "photop/word-game" 
        registryCredential = 'docker_hub'
        dockerImage = ""
    } 
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
		    bat "start/min docker run \"world-game:$BUILD_NUMBER\""
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
	 stage('build and push image') { 	
            steps { 	
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    docker.withRegistry('', registryCredential) {	
                    dockerImage.push() 	
                    }	
                }  	
            }	
        }
	 stage ('Deploy helm'){
            steps{
                script{
                    bat """
		          minikube start
                          helm install test --debug --set image.repostitory=photop33/word-game,image.tag=${BUILD_NUMBER}  world-game-0.1.0.tgz 
		          //helm install word-game-test --dry-run  --debug --set image.repostitory=photop33/word-game,image.tag=${BUILD_NUMBER} test'
		          helm list --all
		          minikube service list 
			  echo success Deploy helm
		        """
		    }  
                }
            }
        stage('e2e') {
            steps {
		    script {
                    bat 'python e2e.py'
                    bat 'echo e2e.py'
                 }
               }
            }
	 stage('create helm chart') {
            steps {
		    script {
                    bat 'helm create world-game'
                    bat 'echo helm crete!'
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
