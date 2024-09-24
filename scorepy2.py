#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


# Importing packages
import requests
import json


# In[2]:


host = "http://sit.woodpecker.com"
username ="akash"
password ="akash@2024"


# In[17]:


#Defining url
url = f"http://sit.woodpecker.com/SASLogon/oauth/token" 

authBody = 'grant_type=password&username=%s&password=%s' %(username, password)

headersAuth={'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

r =  requests.request('POST', url, data= authBody, headers=headersAuth, auth=('sas.ec', ''))

#access_token from postman
token = 'eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vbG9jYWxob3N0L1NBU0xvZ29uL3Rva2VuX2tleXMiLCJraWQiOiJsZWdhY3ktdG9rZW4ta2V5IiwidHlwIjoiSldUIn0.eyJqdGkiOiIzNzQ5Y2I2YTA5NmI0NDA0ODg0NTY4MDJmNGIwYzUzMyIsImV4dF9pZCI6InVpZD1ha2FzaCxvdT1XUCxkYz12aXlhLGRjPWNvbSIsInNlc3Npb25fc2lnIjoiNjNEQThEMzMzNUNFOUFDMTJBRUNEMkQ1ODg4RTU3MDAiLCJhdXRob3JpdGllcyI6WyJEYXRhQWdlbnRQb3dlclVzZXJzIiwiRGF0YUJ1aWxkZXJzIiwiRXNyaVVzZXJzIiwiU0FTQWRtaW5pc3RyYXRvcnMiLCJEYXRhQWdlbnRBZG1pbmlzdHJhdG9ycyJdLCJzdWIiOiJkMTliODNiOS1lMjVhLTQ2MDktYmMxZS1iZWJhNDk1ZTQ0M2YiLCJzY29wZSI6WyJjbGllbnRzLnJlYWQiLCJvcGVuaWQiLCJ1YWEuYWRtaW4iLCJTQVNBZG1pbmlzdHJhdG9ycyIsImNsaWVudHMud3JpdGUiXSwiY2xpZW50X2lkIjoiYXBwXzk5MSIsImNpZCI6ImFwcF85OTEiLCJhenAiOiJhcHBfOTkxIiwiZ3JhbnRfdHlwZSI6InBhc3N3b3JkIiwidXNlcl9pZCI6ImQxOWI4M2I5LWUyNWEtNDYwOS1iYzFlLWJlYmE0OTVlNDQzZiIsIm9yaWdpbiI6ImxkYXAiLCJ1c2VyX25hbWUiOiJha2FzaCIsImVtYWlsIjoiYWthc2hAdml5YS5jb20iLCJhdXRoX3RpbWUiOjE3MjcxODEyMDMsInJldl9zaWciOiJmY2IyN2QyZSIsImlhdCI6MTcyNzE4MTIwMywiZXhwIjoxNzI3MjI0NDAyLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0L1NBU0xvZ29uL29hdXRoL3Rva2VuIiwiemlkIjoidWFhIiwiYXVkIjpbImFwcF85OTEiLCJjbGllbnRzIiwidWFhIiwib3BlbmlkIl19.ZjOYUxdh5dCuZf2ijbHr4HbsFmDAONpAv6b7hv13mVBGG_Fub0_auOcULam9hQfaVLnaV75olOIPG_R75FWfFdJkG1ABbEN7ua-Xm7YMVl3LGtAL7ggw9nMHdzMU0zY-fxu3FX_cydjhxKiPppdfF-lloDoGYZ8pYjQLHuQiWx-w2Unsm5mJMHJH-TPPyguHC0ljpO6Tun8Oxtnl3tAV4AFNO9QLXGhvyu3abjtQdI7IyYzwD3wjI5mD96B2v-FvHKj4Ys2gTubwMj0qMGJzD9kZG2L5w58FKtiqfr2Df4tYJPQxW3lUsKcIrE8ZPlzgKDoN7_M5Fackhx8_tqCs4w'


# In[4]:


#Getting publish model information
headers = {'Authorization': 'Bearer ' + token}

url =f"http://sit.woodpecker.com/microanalyticScore/modules/" 

r = requests.request('GET', url, headers = headers, verify=False)

for key in r.json()['items']:
    print(key['name'].lower())


# In[7]:


#JSON file for selected model
headers = {'Authorization': 'Bearer ' + token}

url =f"http://sit.woodpecker.com/microanalyticScore/modules/decisiontreeclassifier/steps" 

r = requests.request('GET', url, headers = headers, verify=False) 

r.json()


# In[18]:


#Creating sample data for scoring
import requests 
import json # Define all required variables for the scoring 
LOAN = 10000 # Example value
CLAGE = 24 # Example value 
CLNO = 5 # Example value 
YOJ = 10 # Example value (Years on Job)
DELINQ = 0 # Example value
DEBTINC = 30 # Example value 
DEROG = 0 # Example value 
MORTDUE = 150000 # Example value 
VALUE = 200000 # Example value
NINQ = 2 # Example value
# Create the payload with all required fields
payload_dict = { "inputs": [ {"name": "LOAN", "value": LOAN}, 
                            {"name": "CLAGE", "value": CLAGE},
                            {"name": "CLNO", "value": CLNO}, 
                            {"name": "YOJ", "value": YOJ}, 
                            {"name": "DELINQ", "value": DELINQ}, 
                            {"name": "DEBTINC", "value": DEBTINC}, 
                            {"name": "DEROG", "value": DEROG}, 
                            {"name": "MORTDUE", "value": MORTDUE},
                            {"name": "VALUE", "value": VALUE}, 
                            {"name": "NINQ", "value": NINQ} ] } 
# Convert the Python dictionary to a JSON string
payload = json.dumps(payload_dict)
# Define the headers with content type and authorization token 
headers = { 'Content-Type': 'application/vnd.sas.microanalytic.module.step.input+json', 'Authorization': 'Bearer ' + token } 
# Define the URL for the microanalyticScore module
url = f"http://sit.woodpecker.com/microanalyticScore/modules/decisiontreeclassifier/steps/score" 
# Make the POST request with the payload 
try: 
    r = requests.post(url, data=payload, headers=headers, verify=False)
    # Check if the request was successful
    if r.status_code == 200 or r.status_code ==201:
        response = r.json() 
        print("Scoring response:", response)             
    else: 
        print(f"Error: {r.status_code}, Response: {r.text}") 
except requests.exceptions.RequestException as e: print(f"Request failed: {e}")




# In[9]:


#test

import pandas as pd

df = pd.read_csv('hmeq.csv')


# In[12]:


df


# In[15]:


#sampled_hmeq


# In[19]:


#Using data set for model scoring
import pandas as pd
import requests
import json

# Assuming 'hmeq' is your original dataset loaded as a DataFrame
# Sample 100 rows from the original dataset
sampled_hmeq = df.sample(n=100, random_state=42)

# Remove the 'BAD' column
#sampled_hmeq = sampled_hmeq.drop(columns=['BAD']).dropna()

# Assuming 'hmeq' is your original dataset loaded as a DataFrame
# Sample 100 rows from the original dataset
sampled_hmeq = df.sample(n=100, random_state=42)

# Drop the 'BAD' column if it exists, and ignore errors if it doesn't
sampled_hmeq = sampled_hmeq.drop(columns=['BAD'], errors='ignore').dropna()

# Proceed with the rest of your code...


# Define the headers for the scoring API
headers = {
    'Content-Type': 'application/vnd.sas.microanalytic.module.step.input+json',
    'Authorization': 'Bearer ' + token  # Ensure 'token' is defined
}

# Define the URL for the microanalyticScore module
url = f"https://sit.woodpecker.com/microanalyticScore/modules/decisiontreeclassifier/steps/score"

# Iterate over each row in the sampled DataFrame to make scoring requests
for index, row in sampled_hmeq.iterrows():
    # Create the payload for the current row
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

    # Convert the Python dictionary to a JSON string
    payload = json.dumps(payload_dict)

    # Make the POST request
    try:
        r = requests.post(url, data=payload, headers=headers, verify=False)

        # Check if the request was successful
        if r.status_code == 200 or r.status_code == 201:
            response = r.json()
            print(f"Scoring response for row {index}:", response)
        else:
            print(f"Error for row {index}: {r.status_code}, Response: {r.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed for row {index}: {e}")
 



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




