import os
from pathlib import Path
from PIL import Image
from Prompts.prompt import template
from app_secrets import OPENAI_API_KEY
from sql_execution import execute_sf_query
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain import OpenAI, LLMChain, ConversationChain
from langchain.memory import ConversationBufferMemory

# create env variable
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
memory = ConversationBufferMemory(memory_key='history', return_message=True)
root_path = [p for p in Path(__file__).parents if p.parts[-1] == "SQL Generator"][0]

# create front-end using streamlit
st.title("🦜🔗Langchain AI SQL Assistant")
user_input = st.text_input("You: ",
                           placeholder="Your AI assistant here! Ask me anything ...",
                           label_visibility='hidden')
tab_titles = ["Result", "Query", "ER Diagram"]
tabs = st.tabs(tab_titles)

# load the image
erd_image = Image.open(f'{root_path}/images/employees.jpg')
with tabs[2]:
    st.image(erd_image)

# initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
else:
    for message in st.session_state.chat_history:
        memory.save_context({'input': message['human']}, {'output': message['AI']})

# create the prompt
prompt_template = PromptTemplate(input_variables=['history', 'input'],
                                 template=template)

llm = OpenAI(temperature=0.1)

sql_generation_chain = LLMChain(llm=llm,
                                prompt=prompt_template,
                                memory=memory,
                                verbose=True)

if user_input:
    sql_query = sql_generation_chain(user_input)
    result = execute_sf_query(sql_query['text'])
    message = {'human': user_input, 'AI': sql_query['text']}
    st.session_state.chat_history.append(message)
    st.write(sql_query)
    with tabs[0]:
        st.write(result)
    with tabs[1]:
        st.write(sql_query['text'])
    with st.expander(label='Chat History', expanded=False):
        st.write(st.session_state.chat_history)

