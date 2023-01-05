def setBuildStatus(String state, String context, String message) {
    step([
        $class: "GitHubCommitStatusSetter",
        reposSource: [
            $class: "ManuallyEnteredRepositorySource",
            url: "https://github.com/zektorum/atha.yoga.git"
        ],
        contextSource: [
            $class: "ManuallyEnteredCommitContextSource",
            context: context
        ],
        errorHandlers: [[
            $class: "ChangingBuildStatusErrorHandler",
            result: "UNSTABLE"
        ]],
        commitShaSource: [
            $class: "ManuallyEnteredShaSource",
            sha: env.GIT_COMMIT_HASH
        ],
        statusResultSource: [
            $class: 'ConditionalStatusResultSource',
            results: [
                [
                    $class: 'AnyBuildResult',
                    message: message,
                    state: state
                ]
            ]
        ]
    ])
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
                setBuildStatus('PENDING', "build", 'building started')
                try {
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
                } catch (err) {
                    echo "Caught exception: ${err}"
                    setBuildStatus('FAILURE', "build", "build failed")
                    currentBuild.result = 'FAILURE'
                }
                setBuildStatus('SUCCESS', "build", 'building successful')
            }
        }
        stage('Deploy') {
            steps {
                setBuildStatus('PENDING', "deploy", 'deployment started')
                try {
                    sh 'docker-compose --env-file backend/.env up -d'
                } catch (err) {
                    echo "Caught exception: ${err}"
                    setBuildStatus('FAILURE', "deploy", "deployment failed")
                    currentBuild.result = 'FAILURE'
                }
                setBuildStatus('SUCCESS', "deploy", "deployment successful")
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
