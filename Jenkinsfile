pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "yourdockerhubusername/IMT2023513"
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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --disable-warnings'
            }
        }

        stage('Build Docker Image') {
            when { success() }
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
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                    sh 'docker push $DOCKER_IMAGE:latest'
                }
            }
        }
    }
}
