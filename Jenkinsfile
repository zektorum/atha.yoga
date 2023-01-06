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

void setBuildStatus(String message, String state) {
  step([
      $class: "GitHubCommitStatusSetter",
      reposSource: [$class: "ManuallyEnteredRepositorySource", url: "https://github.com/my-org/my-repo"],
      contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
      errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
      statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
  ]);
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
                script {
                    try {
                        publishChecks actions: [[description: 'Building started', identifier: '1. Building', label: 'CI/CD']], summary: 'Building started', status: 'IN_PROGRESS', name: 'Building', title: 'Jenkins CI/CD'
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
                        publishChecks conclusion: 'SUCCESS', summary: 'Building finished', status: 'COMPLETED', name: 'Building', title: 'CI/CD'
                    } catch (err) {
                        echo "Caught exception: ${err}"
                        publishChecks conclusion: 'FAILURE', summary: 'Building failed', status: 'COMPLETED', name: 'Building', title: 'CI/CD'
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    try {
                        publishChecks summary: 'Deployment started', status: 'IN_PROGRESS', name: 'Deployment', title: 'CI/CD'
                        sh 'docker-compose --env-file backend/.env up -d'
                        publishChecks conclusion: 'SUCCESS', summary: 'Deployment successful', status: 'COMPLETED', name: 'Deployment', title: 'CI/CD'
                        setBuildStatus("Build complete", "SUCCESS")
                    } catch (err) {
                        echo "Caught exception: ${err}"
                        publishChecks conclusion: 'FAILURE', summary: 'Deployment failed', status: 'COMPLETED', name: 'Deployment', title: 'CI/CD'
                        currentBuild.result = 'FAILURE'
                    }
                }
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
