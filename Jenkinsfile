pipeline{
    agent any

    stages{
        stage("Cloning the repository from the github"){
            steps{
                git 'https://github.com/Manojkumar1709/python-selenium.git'
            }
        }

        stage('Build') {
            steps {
                bat 'pip install selenium'               
            }
        }

        stage("Running the tests") {
            steps {
               bat 'python test.py'
            }
       }
    }
}