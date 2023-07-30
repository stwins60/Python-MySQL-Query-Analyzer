pipeline {
    agent any
    
    environment {
        
        DOCKERHUB_USERNAME = "tonjei1" 

        IMAGE_NAME = "tonjei1/anthony1_nginx" 

        DEPLOYMENT_NAME = "customer-web" 

        IMAGE_TAG = "${params.BUILD_NUMBER}" 

        DOCKERHUB_CREDENTIALS = credentials('4c207755-df9b-4255-88e1-4bccfe7e4f96') 

        TF_VAR_customer_site_image = "${env.IMAGE_NAME}:${params.BUILD_NUMBER}" 

        AZURE_CREDENTIALS = credentials('3f9658a6-a1a4-4535-b30f-fc541e197275') 

        

        AWS_REGION = "eastus" 
    }
    
    stages {
        stage('Checkout Git Repository') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/tonjei1/Python-MySQL-Query-Analyzer.git']])
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // def imageName = "${env.IMAGE_NAME}:${params.BUILD_NUMBER}"
                    def command = "docker image inspect $imageName"
                    def returnStatus = sh(script:command, returnStatus: true)
                    
                    if (returnStatus == 0) {
                        echo 'Using existing Docker Image'
                    } else {
                        echo 'Building a new Docker Image'
                        def buildCommand = "docker build -t $imageName ."
                        sh(script: buildCommand)
                    }
                }
            }
        }
        
        stage('Logging in to DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                echo 'Login Completed'
            }
        }
        
        stage('Container Audit') {
            steps {
                sh 'wget https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl'
                // sh "trivy image -o report.html ${env.IMAGE_NAME}:${params.BUILD_NUMBER}"
            }
        }
        
        stage('Push Image to DockerHub'){
            steps {
                sh "docker push ${env.IMAGE_NAME}
              // :${params.BUILD_NUMBER}"
                echo 'Push Image Completed'
            }
        }
        
        stage('Deploy to Kubernetes with Terraform') {
            steps {
                        echo 'Configuring Azure'
                        sh AZURE_CREDENTIALS'
                        if(params.ACTION == 'APPLY') {
                            echo "Peforming Terraform Apply"
                            sh 'terraform apply -auto-approve'
                        }
                        else if (params.ACTION == 'DESTROY') {
                            echo "Peforming Terraform Destroy"
                            sh 'terraform destroy -auto-approve'
                        }
                        else {
                            error "Invalid action selected." 
                        }
            }
        }
        
    }
}
