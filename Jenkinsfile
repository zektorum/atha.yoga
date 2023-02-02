def sendEmail(message) {
    emailext body: 'Project built and deployed successfully.',
        subject: 'Atha.Yoga: CI/CD',
        from: 'Jenkins (Atha.Yoga Master Node)',
        to: '${DEFAULT_RECIPIENTS}'
}

def getExitCode(container_name) {
    EXIT_CODE = """${sh(
        script: "docker inspect -f '{{.State.ExitCode}}' ${container_name}",
        returnStdout: true
    )}"""
    return EXIT_CODE
}

def getContainerStatus(container_name) {
    STATUS = """${sh(
        script: "docker inspect -f '{{.State.Status}}' ${container_name}",
        returnStdout: true
    )}"""
    return STATUS
}

pipeline {
    agent any
    environment {
        BRANCH_NAME="develop"
        MASTER_ENV_LINK=credentials('MASTER_ENV_LINK')
        DEVELOP_ENV_LINK=credentials('DEVELOP_ENV_LINK')
        STAGE_ENV_LINK=credentials('STAGE_ENV_LINK')
    }
    stages {
        stage('Build') {
            steps {
                step([$class: 'GitHubCommitStatusSetter', statusResultSource : [$class: 'DefaultStatusResultSource']])
                sh '''
                    wget -O backend/.env.master $MASTER_ENV_LINK
                    wget -O backend/.env.develop $DEVELOP_ENV_LINK
                    wget -O backend/.env.stage $STAGE_ENV_LINK
                    chmod g+w backend/.env.*
                    cat .env/.ci-env.${BRANCH_NAME}.test > .env_file.test
                    cat backend/.env.${BRANCH_NAME} >> .env_file.test
                    cat .env/.ci-env.${BRANCH_NAME} > .env_file
                    cat backend/.env.${BRANCH_NAME} >> .env_file
                    COMPOSE_PROJECT_NAME=${BRANCH_NAME}.test docker-compose --env-file .env_file.test build
                '''
            }
        }
        stage('Run') {
            steps {
                 sh 'COMPOSE_PROJECT_NAME=${BRANCH_NAME}.test docker-compose --env-file .env_file.test -p test \
                     up -d --force-recreate'
            }
        }
        stage('Test') {
            steps {
                script {
                    waitUntil {
                        EXIT_CODE = getExitCode("cypress.${BRANCH_NAME}.test")
                        STATUS = getContainerStatus("cypress.${BRANCH_NAME}.test")
                        if (STATUS == "exited\n" && EXIT_CODE == "0\n") {
                            return true;
                        } else if (STATUS == "exited\n" && !(EXIT_CODE == "0\n")) {
                            publishHTML([
                                alwaysLinkToLastBuild: true, keepAll: true,
                                reportDir: 'frontend/tests/cypress/reports/html/', reportFiles: 'index.html',
                                reportName: 'Test report', reportTitles: 'The Report'
                            ])
                            return true;
                        } else {
                            return false
                        }
                    }
                }
            }
        }
        stage('Inspect containers') {
            steps {
                script {
                   def containers = "backend frontend elasticsearch db redis dozzle rabbitmq flower".split(" ")
                   for (container in containers) {
                        STATUS = getContainerStatus("${container}.${BRANCH_NAME}.test")
                        if (STATUS == "exited\n") {
                            sh 'COMPOSE_PROJECT_NAME=${BRANCH_NAME}.test docker-compose --env-file .env_file.test \
                                -p test down'
                            error "${container}.${BRANCH_NAME}.test failed. Exiting..."
                        }
                   }
                   sh 'COMPOSE_PROJECT_NAME=${BRANCH_NAME}.test docker-compose --env-file .env_file.test -p test down'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'COMPOSE_PROJECT_NAME=${BRANCH_NAME}.test docker-compose --env-file .env_file build'
                sh "COMPOSE_PROJECT_NAME=${BRANCH_NAME} docker-compose --env-file .env_file -p ${BRANCH_NAME} \
                    up -d --force-recreate"
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
        always {
            step([$class: 'GitHubCommitStatusSetter', statusResultSource : [$class: 'DefaultStatusResultSource']])
        }
    }
}