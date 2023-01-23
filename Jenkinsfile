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
                    COMPOSE_PROJECT_NAME=${BRANCH_NAME}.test docker-compose --env-file backend/.env.${BRANCH_NAME} build
                '''
            }
        }
        stage('Run') {
            steps {
                 sh 'COMPOSE_PROJECT_NAME=${BRANCH_NAME}.test docker-compose --env-file backend/.env.${BRANCH_NAME} up -d'
            }
        }
        stage('Test') {
            steps {
                script {
                    waitUntil {
                        EXIT_CODE = getExitCode("2cypress-${BRANCH_NAME}")
                        STATUS = getContainerStatus("2cypress-${BRANCH_NAME}")
                        if (STATUS == "exited\n" && EXIT_CODE == "0\n") {
                            sh 'COMPOSE_PROJECT_NAME=${BRANCH_NAME}.test docker-compose --env-file backend/.env.${BRANCH_NAME} down'
                            return true;
                        } else if (STATUS == "exited\n" && !(EXIT_CODE == "0\n")) {
                            sh 'COMPOSE_PROJECT_NAME=${BRANCH_NAME}.test docker-compose --env-file backend/.env.${BRANCH_NAME} down'
                            error 'Failed, exiting now...'
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
                   def containers = "2backend 2frontend 2cypress 2elasticsearch 2db 2redis 2dozzle 2rabbitmq 2flower".split(" ")
                   for (container in containers) {
                        STATUS = getContainerStatus("${container}-${BRANCH_NAME}")
                        if (STATUS == "exited\n") {
                            sh 'COMPOSE_PROJECT_NAME=${BRANCH_NAME}.test docker-compose --env-file backend/.env.${BRANCH_NAME} down'
                            error "${container}-${BRANCH_NAME} failed. Exiting..."
                        }
                   }
                   sh 'COMPOSE_PROJECT_NAME=${BRANCH_NAME}.test docker-compose --env-file backend/.env.${BRANCH_NAME} down'
                }
            }
        }
        stage('Deploy') {
            steps {
                sh "COMPOSE_PROJECT_NAME=${BRANCH_NAME} docker-compose --env-file backend/.env.${BRANCH_NAME} up -d"
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