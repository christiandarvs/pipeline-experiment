pipeline {
    agent { docker { image 'python:3.13.5-alpine3.22' } }

        stages {
            stage('Build') {
                steps{
                    echo "Building Phase"
                    sh "python my_os.py"
                }
            }       
            stage('Test') {
                steps {
                    echo "Testing Phase"
                }
            }
        }
    
}