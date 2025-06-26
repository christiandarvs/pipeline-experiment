pipeline {
    agent { 
        docker {
            image 'python:3.13.5-alpine3.22' 
            args '-u root' 
        }
    }

        stages {
            stage('Build') {
                steps{
                    echo "Building Phase"
                    sh "pip install --no-cache-dir -r requirements.txt"
                    sh "python my_os.py"
                    sh "python get_ocr.py"
                    sh "get_status_code.py"

                }
            }       
            stage('Test') {
                steps {
                    echo "Testing Phase"
                }
            }
        }
    
}