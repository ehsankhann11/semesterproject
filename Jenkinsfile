pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/ehsankhann11/semesterproject.git'
            }
        }

        stage('Deploy HTML') {
            steps {
                // Copy HTML file to a public directory
                sh '''
                sudo cp index.html /var/www/html/index.html
                '''
            }
        }
    }
}
