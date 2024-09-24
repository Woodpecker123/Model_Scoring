pipeline {
  agent any
  stages {
    
    // First stage: Print a message
    stage('Hello') {
      steps {
        echo 'Hi There please work'
      }
    }
      stage('Prepare Python Environment') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv venv'
                    // Activate the virtual environment and install requirements
                    sh '''
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r /usr/share/doc/python3-setuptools-39.2.0/requirements.txt
                    pip install pandas
                    '''
                }
            }
        }
     stage('Setup') {
            steps {
                script {
                    // Define variables
                    env.HOST = "http://sit.woodpecker.com"
                    env.USERNAME = "akash"
                    env.PASSWORD = "akash@2024"
                }
            }
        }
    stage('Authenticate') {
            steps {
                script {
                    def authScript = '''
import requests
import json

host = "${HOST}"
username = "${USERNAME}"
password = "${PASSWORD}"

url = f"http://sit.woodpecker.com/SASLogon/oauth/token"
authBody = f'grant_type=password&username=akash&password=akash@2024'
headersAuth = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

r = requests.post(url, data=authBody, headers=headersAuth, auth=('sas.ec', ''))

if r.status_code == 200:
    token = r.json().get('access_token')
    print(token)
else:
    print(f"Error: {r.status_code}, Response: {r.text}")
                    '''

                    writeFile file: 'auth.py', text: authScript
                    def tokenOutput = sh(script: 'source venv/bin/activate && python3 auth.py', returnStdout: true)
                    env.TOKEN = tokenOutput.trim()
                }
            }
        }
        stage('Get Models') {
            steps {
                script {
                    def modelScript = '''
import requests

token = "${TOKEN}"
headers = {'Authorization': 'Bearer ' + token}
url = f"http://sit.woodpecker.com/microanalyticScore/modules/"
r = requests.get(url, headers=headers, verify=False)

if r.status_code == 200:
    for key in r.json()['items']:
        print(key['name'].lower())
else:
    print(f"Error: {r.status_code}, Response: {r.text}")
                    '''

                    writeFile file: 'get_models.py', text: modelScript
                    sh 'source venv/bin/activate && python3 get_models.py'
                }
            }
        }

        stage('Sample Data') {
            steps {
                script {
                    def sampleScript = '''
import pandas as pd

df = pd.read_csv('hmeq.csv')
if 'BAD' in df.columns:
    sampled_hmeq = df.sample(n=100, random_state=42).drop(columns=['BAD']).dropna()
else:
    sampled_hmeq = df.sample(n=100, random_state=42).dropna()

sampled_hmeq.to_csv('sampled_data.csv', index=False)
                    '''

                    writeFile file: 'sample_data.py', text: sampleScript
                    sh 'source venv/bin/activate && python3 sample_data.py'
                }
            }
        }

        stage('Score Models') {
            steps {
                script {
                    def scoreScript = '''
import pandas as pd
import requests
import json

token = "${TOKEN}"
echo 'token'
headers = {
    'Content-Type': 'application/vnd.sas.microanalytic.module.step.input+json',
    'Authorization': 'Bearer ' + token
}
url = f"http://sit.woodpecker.com/microanalyticScore/modules/decisiontreeclassifier/steps/score"

df = pd.read_csv('sampled_data.csv')

for index, row in df.iterrows():
    payload_dict = {
        "inputs": [
            {"name": "LOAN", "value": row['LOAN']},
            {"name": "CLAGE", "value": row['CLAGE']},
            {"name": "CLNO", "value": row['CLNO']},
            {"name": "YOJ", "value": row['YOJ']},
            {"name": "DELINQ", "value": row['DELINQ']},
            {"name": "DEBTINC", "value": row['DEBTINC']},
            {"name": "DEROG", "value": row['DEROG']},
            {"name": "MORTDUE", "value": row['MORTDUE']},
            {"name": "VALUE", "value": row['VALUE']},
            {"name": "NINQ", "value": row['NINQ']}
        ]
    }
    payload = json.dumps(payload_dict)

    r = requests.post(url, data=payload, headers=headers, verify=False)

    if r.status_code == 200 or r.status_code == 201:
        response = r.json()
        print(f"Scoring response for row {index}:", response)
    else:
        print(f"Error for row {index}: {r.status_code}, Response: {r.text}")
                    '''

                    writeFile file: 'score_models.py', text: scoreScript
                    sh 'source venv/bin/activate && python3 score_models.py'
                }
            }
        }

    
  }
}
