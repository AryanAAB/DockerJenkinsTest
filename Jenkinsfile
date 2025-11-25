pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "awesome3112760/imt2023513"
    }

    stages {

        stage('Pull Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'DockerJenkinsTest',
                    url: 'https://github.com/AryanAAB/DockerJenkinsTest.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    export PYTHONPATH=$PYTHONPATH:$(pwd)
                    pytest --disable-warnings
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:latest .'
                sh 'docker images'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds-Jenkins-Docker-test',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $DOCKER_IMAGE:latest
                    '''
                }
            }
        }
    }
}
