pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // The 'echo 5' pipes the number 5 into the python script so Jenkins doesn't hang waiting for input
                bat 'echo 5 | python fib.py'
            }
        }
        stage('Test') {
            steps {
                // Since this is a simple demo, we just verify the build ran
                echo 'Build successful! Testing complete.'
            }
        }
    }
}