pipeline {
  agent any
  stages {
    stage('CheckVersion') {
      steps {
          sh 'python3 --version'
          sh 'pip install pandas'
      }
    }
     stage('Scoring Model') {
      steps {
       
        sh 'python3 scorepy2.py'
      }
    }

  }
}
