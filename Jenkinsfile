pipeline {
  agent any
  stages {
    stage('checkversion') {
      steps {
          sh 'python3 --version'
          sh 'pip install pandas'
      }
    }
     stage('run python') {
      steps {
       
        sh 'python3 score2.py'
      }
    }

  }
}
