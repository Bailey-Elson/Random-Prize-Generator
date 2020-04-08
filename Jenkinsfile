pipeline{
    agent any

    stages {
        stage('Run locally'){
            steps{
                sh 'python3 ~/workspace/SFIA2/Service1/app.py'
                sh 'python3 ~/workspace/SFIA2/Service2/app.py'
                sh 'python3 ~/workspace/SFIA2/Service3/app.py'
                sh 'python3 ~/workspace/SFIA2/Service4/app.py'
            }
        }
        stage('Development Enviroment'){
            steps{

                sh 'chmod +x ./script/*'
                sh './script/ansible.sh'
                sh './script/docker.sh'
                
            }
        }
        stage('Testing'){
            steps{
                sh './script/test.sh'
            }
        }
    }
}