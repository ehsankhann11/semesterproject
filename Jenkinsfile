pipeline {
    agent any

    environment {
        EC2_USER = 'ec2-user'           // Change if using Ubuntu (use 'ubuntu')
        EC2_IP = 'YOUR_EC2_PUBLIC_IP'   // Replace with your EC2 instance's public IP
        PEM_PATH = '/path/to/your-key.pem' // Absolute path to your .pem key on Jenkins server
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'echo "No tests defined yet."'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh '''
                scp -o StrictHostKeyChecking=no -i $PEM_PATH app.py requirements.txt index.html $EC2_USER@$EC2_IP:/home/$EC2_USER/
                ssh -o StrictHostKeyChecking=no -i $PEM_PATH $EC2_USER@$EC2_IP << EOF
                    pkill -f app.py || true
                    pip3 install -r requirements.txt
                    nohup python3 app.py > output.log 2>&1 &
                EOF
                '''
            }
        }
    }
}
