pipeline {
    agent any
   stages{
        stage ("git checkout"){
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Abayomi-Git', url: 'https://github.com/YomiPounds/Idris-Python-MySQL-Query-Analyzer.git']])
            }
        }
        stage ("docker build stage"){
            steps {
                sh "docker build -t yomipounds/yomi-jenkins-image ."
            }
        }
        stage("docker login"){
            steps{
                sh "docker login -u yomipounds -p Devops2022"
            }
        }
        stage("docker tag and push to hub"){
            steps{
                sh "docker tag yomipounds/yomi-jenkins-image:latest yomipounds/yomi-jenkins-image:1"
                sh "docker push yomipounds/yomi-jenkins-image:1"
            }
        }
    }
}
