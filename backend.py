from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from prompts import build_prompt
import streamlit as st





key=open("api.txt").read().strip()

model=ChatOpenAI(api_key=key,model="gpt-4o-mini",temperature=0.5)

# prompt_text = build_prompt(task, user_input, **kwargs)

# prompt= ChatPromptTemplate.from_template(prompt_text)


output=StrOutputParser()


# chain = prompt | model | output
 
# def llm (prompt):
#   result=chain.invoke(prompt)
#   return result

def llm(task: str, user_input: str, **kwargs):  # arguments yahan lo
    prompt_text = build_prompt(task, user_input, **kwargs)  # ab defined hai
    prompt = ChatPromptTemplate.from_template(prompt_text)
    chain = prompt | model | output  # chain andar banao
    result = chain.invoke({})
    return result