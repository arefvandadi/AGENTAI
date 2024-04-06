# API Key
import os
import openai
openai.api_key = os.getenv('OPENAI_API_KEY_1')

import pandas as pd
population_path = os.path.join('data', 'WorldPopulation2023.csv')
population_df = pd.read_csv(population_path)
print(population_df.head())




