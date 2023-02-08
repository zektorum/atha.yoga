def sendEmail(message) {
    emailext body: message,
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
    parameters {
        booleanParam(name: 'REFRESH_DATABASE', defaultValue: false,
            description: 'Fully resets database, migrates and creates test data.')
        choice(name: 'BUILD_MODE', choices: ['Default', 'Test pipeline'],
            description: ''
        )
    }
    environment {
        BRANCH_NAME = "${env.BRANCH_NAME}"
        MASTER_ENV_LINK = credentials('MASTER_ENV_LINK')
        DEVELOP_ENV_LINK = credentials('DEVELOP_ENV_LINK')
        STAGE_ENV_LINK = credentials('STAGE_ENV_LINK')
        CI_ENV_FILENAME = ""
        CI_TEST_ENV_FILENAME = ""
        PROJECT_NAME = ""
        TESTING_PROJECT_NAME = ""
    }
    stages {
        stage('Build') {
            steps {
                step([$class: 'GitHubCommitStatusSetter', statusResultSource : [$class: 'DefaultStatusResultSource']])
                echo 'Downloading env files...'
                sh '''
                    wget -O backend/.env.master $MASTER_ENV_LINK
                    wget -O backend/.env.develop $DEVELOP_ENV_LINK
                    wget -O backend/.env.stage $STAGE_ENV_LINK
                '''
                echo 'Setting up build mode...'
                script {
                    if (params.BUILD_MODE == "Default") {
                        echo 'Build mode: Default'
                        CI_ENV_FILENAME = ".env/.ci-env.${BRANCH_NAME}"
                        CI_TEST_ENV_FILENAME = ".env/.ci-env.${BRANCH_NAME}.test"
                        PROJECT_NAME = "${BRANCH_NAME}"
                        TESTING_PROJECT_NAME = "${BRANCH_NAME}.test"
                    } else if (params.BUILD_MODE == "Test pipeline") {
                        echo 'Build mode: Test pipeline'
                        CI_ENV_FILENAME = ".env/.ci-testing-env"
                        CI_TEST_ENV_FILENAME = ".env/.ci-testing-env.test"
                        PROJECT_NAME = "ci-testing.${BRANCH_NAME}"
                        TESTING_PROJECT_NAME = "ci-testing.test"
                    }
                }
                echo 'Setting up environment...'
                sh """
                    cat backend/.env.$BRANCH_NAME > backend/.env.test
                    cat $CI_TEST_ENV_FILENAME >> backend/.env.test
                    cat $CI_ENV_FILENAME > backend/.env
                    cat backend/.env.$BRANCH_NAME >> backend/.env
                    echo REFRESH_DATABASE=$REFRESH_DATABASE >> backend/.env
                    chmod g+w backend/.env.*
                """
                echo 'Building test environment...'
                sh "COMPOSE_PROJECT_NAME=$TESTING_PROJECT_NAME docker-compose --env-file backend/.env.test \
                    -p $TESTING_PROJECT_NAME build"
            }
        }
        stage('Run') {
            steps {
                echo 'Running test environment...'
                 sh "COMPOSE_PROJECT_NAME=$TESTING_PROJECT_NAME docker-compose --env-file backend/.env.test \
                     -p $TESTING_PROJECT_NAME up -d --force-recreate"
            }
        }
        stage('Test') {
            steps {
                script {
                    echo 'Testing started...'
                    waitUntil {
                        EXIT_CODE = getExitCode("cypress.${TESTING_PROJECT_NAME}")
                        STATUS = getContainerStatus("cypress.${TESTING_PROJECT_NAME}")
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
                        STATUS = getContainerStatus("${container}.${TESTING_PROJECT_NAME}")
                        if (STATUS == "exited\n") {
                            sh "COMPOSE_PROJECT_NAME=$TESTING_PROJECT_NAME docker-compose --env-file backend/.env.test \
                                -p $TESTING_PROJECT_NAME down"
                            error "${container}.${TESTING_PROJECT_NAME} failed. Exiting..."
                        }
                   }
                   echo 'Testing was successful. Stopping test environment...'
                   sh "COMPOSE_PROJECT_NAME=$TESTING_PROJECT_NAME docker-compose --env-file backend/.env.test \
                       -p $TESTING_PROJECT_NAME down"
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Building project environment...'
                sh "COMPOSE_PROJECT_NAME=$PROJECT_NAME docker-compose --env-file backend/.env \
                    -p $PROJECT_NAME up -d --build --force-recreate"
            }
        }
    }
    post {
        success {
            sendEmail('Project built and deployed successfully.')
        }
        failure {
            sendEmail('Something went wrong.\n\nProject: $JOB_NAME\nBuild Number: $BUILD_NUMBER\nURL: $BUILD_URL')
        }
        always {
            step([$class: 'GitHubCommitStatusSetter', statusResultSource : [$class: 'DefaultStatusResultSource']])
        }
    }
}