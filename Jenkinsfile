pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
    post {
        success {
            emailext body: 'Project built and deployed successfully.',
                    subject: 'Atha.Yoga: CI/CD',
                    from: 'Jenkins (Atha.Yoga Master Node)',
                    to: '${DEFAULT_RECIPIENTS}'
        }
        failure {
            emailext body: "Something went wrong.",
                    subject: 'Atha.Yoga: CI/CD',
                    from: 'Jenkins (Atha.Yoga Master Node)',
                    to: '${DEFAULT_RECIPIENTS}'
        }
    }
}