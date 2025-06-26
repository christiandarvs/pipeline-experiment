pipeline {
    agent any

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