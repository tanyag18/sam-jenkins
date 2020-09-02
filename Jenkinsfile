pipeline {
    agent { docker { image 'python:3.8' } }
    stages {
        stage('test') {
            steps {
                bat 'echo "testing applicationa"'
                //bat 'python --version' 
                //bat 'python function\\test_calc.py'

            }
        }

        // stage('build') {
        //     steps {
        //         bat 'echo "building package"'
        //         bat 'sam package --template-file template.yaml --output-template-file deploy-calc.yaml --s3-bucket sam-jenkins-init --region us-east-1'
                
        //     }
        // }
        // stage('deploy') {
        //     steps {
        //         bat 'echo "deploying"'
        //         bat 'sam deploy --template-file deploy-calc.yaml --stack-name sam-jenkins-stack --no-confirm-changeset --capabilities CAPABILITY_IAM --region us-east-1'
                
        //     }
        // }
    }
}