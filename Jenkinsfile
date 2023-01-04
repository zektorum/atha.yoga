def setBuildStatus(state, message, context){
    withCredentials([string(credentialsId: 'github-commit-status-token', variable: 'TOKEN')]) {
        sh 'curl -X POST -H "Accept: application/vnd.github+json" -H "Authorization: Bearer $TOKEN"  -H "X-GitHub-Api-Version: 2022-11-28"  https://api.github.com/repos/zektorum/atha.yoga/statuses/\\$(git rev-parse HEAD) -d \'{"state":"success","description":"$message"},"context":"$context"}\''
    }
}

def sendEmail(message) {
    emailext body: 'Project built and deployed successfully.',
        subject: 'Atha.Yoga: CI/CD',
        from: 'Jenkins (Atha.Yoga Master Node)',
        to: '${DEFAULT_RECIPIENTS}'
}

def publishReport() {
    publishHTML (target : [allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: 'frontend/tests/reports/html',
        reportFiles: 'index.html',
        reportTitles: 'My Reports',
        reportName: 'Frontend testing report',
        reportTitles: 'My Reports'])
}

pipeline {
    agent any
    stages {
        stage('Build') {
            environment {
                BRANCH_NAME="develop"
                MASTER_ENV_LINK=credentials('MASTER_ENV_LINK')
                DEVELOP_ENV_LINK=credentials('DEVELOP_ENV_LINK')
                STAGE_ENV_LINK=credentials('STAGE_ENV_LINK')
            }
            steps {
                setBuildStatus('pending', 'Building started.', 'Jenkins CI/CD')
                sh '''
                    wget -O backend/.env.master $MASTER_ENV_LINK
                    chmod g+w backend/.env.master
                    wget -O backend/.env.develop $DEVELOP_ENV_LINK
                    chmod g+w backend/.env.develop
                    wget -O backend/.env.stage $STAGE_ENV_LINK
                    chmod g+w backend/.env.stage
                    cp backend/.env.$BRANCH_NAME backend/.env
                    docker-compose --env-file backend/.env build
                '''
                setBuildStatus('success', 'Built successfully.', 'Jenkins CI/CD')

            }
        }
        stage('Deploy') {
            steps {
                setBuildStatus('pending', 'Deploymend started.', 'Jenkins CI/CD')
                sh 'docker-compose --env-file backend/.env up -d'
                setBuildStatus('success', 'Deployed successfully.', 'Jenkins CI/CD')
            }
        }
    }
    post {
        success {
            sendEmail('Project built and deployed successfully.')
        }
        failure {
            sendEmail('Something went wrong.')
        }
    }
}
