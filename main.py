from prompt import instruction_str, new_prompt
from note_engine import note_engine

# API Key
import os
import openai
openai.api_key = os.getenv('OPENAI_API_KEY_1')

# Import population csv file 
import pandas as pd
population_path = os.path.join('data', 'WorldPopulation2023.csv')
population_df = pd.read_csv(population_path)
print(population_df.head())

# Defining a Query Engine
from llama_index.core.query_engine import PandasQueryEngine
panda_query_engine = PandasQueryEngine(df=population_df, verbose=True, 
                                    instruction_str=instruction_str,
                                    pandas_prompt=new_prompt, 
                                    )
# Manual Query
# panda_query_engine.query(
#     'What is the 34th ranked country based on population?'
#     )

# defined tools and ReActAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
tools = [
    note_engine,
    QueryEngineTool(
        query_engine=panda_query_engine,
        metadata=ToolMetadata(
            name='population_data',
            description="This gives information at the world populationa and demographic",
        )
    )
]

llm = OpenAI(model='gpt-3.5-turbo')
agent = ReActAgent.from_tools(tools=tools, llm=llm, verbose=True)




