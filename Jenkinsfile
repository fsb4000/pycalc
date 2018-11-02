pipeline {
    agent {label 'python'}
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage("Run") {
            steps {
                sh "python3 calculator.py  1 5"
            }
        }
        stage("Unit test") {
            steps {
                sh "python3 -m unittest test_calculator.py"
            }
        }
    }
}
