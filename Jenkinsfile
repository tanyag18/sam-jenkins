pipeline {
    agent any//{ docker { image 'python:3.5.1' } }
    stages {
        stage('test') {
            steps {
                //sh 'python --version'
                bat 'echo "testing app"'
                
            }
        }

        stage('build') {
            steps {
                //sh 'python --version'
                bat 'echo "building package"'
                bat 'sam package --template-file template.yaml --output-template-file deploy-calc.yaml --s3-bucket sam-calc-init'
                
            }
        }
        stage('deploy') {
            steps {
                // sh 'python --version'
                bat 'echo "deploying"'
                bat 'sam deploy --template-file deploy-calc.yaml --stack-name sam-test-stack --no-confirm-changeset --capabilities CAPABILITY_IAM'
                
            }
        }
    }
}