  
pipeline{
    agent any

    stages {
        stage('Development Enviroment'){
            steps{

                sh 'chmod +x ./script/*'
                sh './script/ansible.sh'
                // sh './script/docker.sh'
                
            }
        }
        stage('Testing'){
            steps{
                sh './script/test.sh'
            }
        }
    }
}