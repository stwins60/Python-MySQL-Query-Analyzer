pipeline {
    agent any
    parameters {
          string defaultValue: 'Abayomi', description: 'Who is working this?', name: 'AUTHOR', trim: true
          choice choices: ['yomipounds/yomi1', 'yomipounds/yomi2', 'yomipounds/yomi3'], description: 'what image name to use for this build', name: 'IMAGE'
        }
   stages{
        stage ("git checkout"){
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Abayomi-Git', url: 'https://github.com/YomiPounds/Idris-Python-MySQL-Query-Analyzer.git']])
            }
        }
        stage ("docker build stage"){
            steps {
                sh "docker build -t ${params.IMAGE} ."
            }
        }
        stage("docker login"){
            steps{
                sh "docker login -u yomipounds -p Devops2022"
            }
        }
        stage("docker tag, push to hub and run container"){
            steps{
                sh "docker tag ${params.IMAGE}:latest ${params.IMAGE}:1"
                sh "docker push ${params.IMAGE}:1"
                sh "docker run -d --name yomi-contains -p 5004-5000 ${params.IMAGE}"
            }
        }
        stage("deploy to k8s cluster"){
            steps{
                dir('./k8s') {
                    sh "kubectl apply -f ."
                }
            }
        }
    }
}
