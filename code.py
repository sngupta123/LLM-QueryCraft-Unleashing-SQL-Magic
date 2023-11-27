import os
from pathlib import Path
from PIL import Image
from app_secrets import OPENAI_API_KEY
from sql_execution import execute_sf_query
import streamlit as st
from langchain.prompts import load_prompt
from langchain import OpenAI, LLMChain

# create env variable
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
root_path = [p for p in Path(__file__).parents if p.parts[-1] == "SQL Generator"][0]

# create front-end using streamlit
st.title("🦜🔗Langchain AI SQL Assistant")
user_input = st.text_input("Enter your question here")
tab_titles = ["Result", "Query", "ER Diagram"]
tabs = st.tabs(tab_titles)

# load the image
erd_image = Image.open(f'{root_path}/images/employees.jpg')
with tabs[2]:
    st.image(erd_image)

# create the prompt
prompt_template = load_prompt(f'{root_path}/Prompts/tpch_prompt.yaml')

llm = OpenAI(temperature=0.1)
sql_generation_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)

if user_input:
    sql_query = sql_generation_chain(user_input)
    result = execute_sf_query(sql_query['text'])
    with tabs[0]:
        st.write(result)
    with tabs[1]:
        st.write(sql_query['text'])

