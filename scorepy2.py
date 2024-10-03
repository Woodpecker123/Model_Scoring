import sasctl
import pandas as pd
from sasctl import Session
from sasctl import publish_model
from sasctl.services import microanalytic_score as mas
from sasctl.services import model_repository as mrb

# Create a session
session = Session('https://sit.woodpecker.com', 'akash', 'akash@2024', verify_ssl=False)

# Publish the model
model = "LG_Test3"
module = publish_model(model, 'maslocal')
print(module)

# Read the input data
df = pd.read_csv('donor_score.csv')
sampled_df = df
scored_results = []

# Score each row
for index, row in sampled_df.iterrows():
    try:
        response = module.score(**row.to_dict())

        if isinstance(response, tuple):
            EM_CLASSIFICATION = response[0]
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
        print(f"Error scoring row {index}: {e}")

# Create a DataFrame for the scored results
scored_df = pd.DataFrame(scored_results)

# Save the scored DataFrame to a CSV file in the specified location
output_file = '/var/lib/jenkins/scored_results.csv'
scored_df.to_csv(output_file, index=False)

print(f"Scored results saved to {output_file}")

