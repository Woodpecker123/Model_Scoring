import sasctl
import pandas as pd
from sasctl import Session
from sasctl import publish_model
from sasctl.services import microanalytic_score as mas
from sasctl.services import model_repository as mrb
session = Session('https://sit.woodpecker.com','akash','akash@2024',verify_ssl=False)
model = "LG_Test2"
module = publish_model(model,'maslocal')
print(module)
df = pd.read_csv('donor_score.csv')
sampled_df = df
scored_results =[]

for index , row in sampled_df.iterrows():
    try:
        response = module.score(**row.to_dict())
        
        if isinstance(response,tuple):
            EM_CLASSIFICATION  = response[0]
            EM_EVENTPROBABILITY = response[1]
        else:
            EM_CLASSIFICATION = response['EM_CLASSIFICATION']
            EM_EVENTPROBABILITY = response['EM_EVENTPROBABILITY']
    
        scored_results.append({
        **row.to_dict(),
        'EM_CLASSIFICATION': EM_CLASSIFICATION,
        'EM_EVENTPROBABILITY': EM_EVENTPROBABILITY
    })
    except Exception as e:
        print(f"Error scoring row {index}:{e}")
        
scored_df = pd.DataFrame(scored_results) 
scored_df.head()
