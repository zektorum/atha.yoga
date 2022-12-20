def setBuildStatus(state, message, context){
    withCredentials([string(credentialsId: 'github-commit-status-token', variable: 'TOKEN')]) {
        sh '''
            curl \\
                -X POST \\
                -H "Accept: application/vnd.github+json" \\
                -H "Authorization: Bearer $TOKEN"\\
                -H "X-GitHub-Api-Version: 2022-11-28" \\
                https://api.github.com/repos/om2c0de/atha.yoga/statuses/\$(git rev-parse HEAD) \\
                -d \'{"state":"$state","description":"$message","context":"$context"}\'
        '''
    }
}

pipeline {
    agent any
    stages {
        stage('Build') {
            environment {
                BRANCH_NAME='${env.BRANCH_NAME}'
                MASTER_ENV_LINK=credentials('MASTER_ENV_LINK')
                DEVELOP_ENV_LINK=credentials('DEVELOP_ENV_LINK')
                STAGE_ENV_LINK=credentials('STAGE_ENV_LINK')
            }
            steps {
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
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose --env-file backend/.env up -d'
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
            emailext body: 'Something went wrong.',
                    subject: 'Atha.Yoga: CI/CD',
                    from: 'Jenkins (Atha.Yoga Master Node)',
                    to: '${DEFAULT_RECIPIENTS}'
        }
    }
}