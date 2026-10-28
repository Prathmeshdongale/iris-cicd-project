pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t iris-classifier .'
            }
        }

        stage('Deploy Application') {
            steps {
                bat '''
                    docker rm -f iris-app 2>NUL
                    docker run -d --name iris-app -p 5000:5000 iris-classifier
                '''
            }
        }
    }

    post {
        success {
            echo 'Build and deployment completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check the Jenkins console output.'
        }
    }
}