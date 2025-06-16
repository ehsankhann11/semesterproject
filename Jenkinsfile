pipeline {
    agent any

    environment {
        APP_DIR = "/home/azureuser/myapp"  // Update this if your directory is different
        VENV_PATH = "${APP_DIR}/venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ehsankhann11/semesterproject.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    cd $APP_DIR
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    cd $APP_DIR
                    source venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Package App') {
            steps {
                sh '''
                    cd $APP_DIR
                    zip -r flask_app_package.zip . -x "venv/*"
                '''
            }
        }

        stage('Deploy App') {
            steps {
                sh '''
                    cd $APP_DIR
                    source venv/bin/activate
                    nohup python app.py > output.log 2>&1 &
                '''
            }
        }
    }
}
