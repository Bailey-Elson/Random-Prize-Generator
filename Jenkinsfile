pipeline{
    agent any

    stages{
        stage("testingInstall"){
            steps{
                sh 'echo "installing docker locally"'
                // sh 'sudo apt-get remove docker docker-engine docker.io -y'
                sh 'sudo apt update -y'
                sh 'sudo apt-get install apt-transport-https'
                sh 'sudo apt-get install ca-certificates'
                sh 'sudo apt-get install curl'
                sh 'sudo apt-get install gnupg-agent'
                sh 'sudo apt-get install software-properties-common'
                sh 'sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -'
                sh 'sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"'
                sh 'sudo apt-get install docker-ce docker-ce-cli containerd.io'
                sh 'sudo systemctl start docker'
                sh 'sudo systemctl enable docker'
                sh 'sudo systemctl status docker'
                sh 'sudo usermod -aG docker $USER'
            }
        }
        stage("testing docker swarm"){
            steps{
                sh 'echo "install testing docker-swarm"'
                sh 'pip3 install pytest'
                sh 'pip3 install coverage'
                sh 'pip3 install -r /var/lib/jenkins/workspace/pipeline2/requirements.txt'
                sh 'sudo docker swarm init'
                sh 'sudo docker stack deploy --compose-file /var/lib/jenkins/workspace/pipeline2/testing-docker-swarm.yml stackdemo'
                sh 'sudo docker stack rm service stackdemo'
                sh 'sudo docker swarm leave -f'
                sh 'sleep 10'
            }
        }
        stage("environment-setting"){
            steps{
                sh 'ansible-playbook -i docker.conf docker-installation.yml'
                sh 'echo "docker install"'
            }
        }
        stage("nodes-assigned"){
            steps{
                sh 'ansible-playbook -i docker.conf assign-nodes.yml'
                sh 'echo "Nodes assigned"'
            }
        }
        stage("depoly-swarm"){
            steps{
                sh 'ansible-playbook -i docker.conf deploy-swarm.yml'
                sh 'echo "swarm depolyed"'
            }
        }
    }
}   