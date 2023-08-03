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
    }
}
