pipeline {
    agent any
   stages{
        stage ("git checkout"){
            steps{
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'Abayomi-Git', url: 'https://github.com/YomiPounds/Idris-Python-MySQL-Query-Analyzer.git']])
            }
        }
    }
}
