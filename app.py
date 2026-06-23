import streamlit as st
from prompts import build_prompt
from backend import llm


st.set_page_config(page_title="AI Utility App", page_icon="🤖")

st.title("🤖 Universal AI Utility")
st.write("Select a task, enter your input, and let AI do the work.")
st.divider()

st.write('Select Task')
task=st.selectbox('task',["Summarize Text", "Translate Text", "Explain Topic", "Generate Email", "Rewrite Content"])
# user_input=st.text_input(" ")
# target_language=st.selectbox('lenguage',["English","Hinglish","marathi","hindi"])


# ── Dynamic inputs based on task ─────────────────────────
user_input = ""
target_language = ""
email_tone = ""
rewrite_style = ""
 
if task == "Summarize Text":
    user_input = st.text_area("Paste the text you want to summarize", height=200)
 
elif task == "Translate Text":
    user_input = st.text_area("Enter the text you want to translate", height=150)
    target_language = st.selectbox(
        "Translate to",
        ["Hindi", "Marathi", "Hinglish", "French", "Spanish", "German", "Japanese"]
    )
 
elif task == "Explain Topic":
    user_input = st.text_input("Enter the topic you want explained (e.g. Black Holes, Recursion)")
 
elif task == "Generate Email":
    user_input = st.text_area("Describe the email you need (e.g. follow up with client about delay)", height=150)
    email_tone = st.selectbox("Email Tone", ["Professional", "Friendly", "Formal", "Apologetic"])
 
elif task == "Rewrite Content":
    user_input = st.text_area("Paste the content you want rewritten", height=200)
    rewrite_style = st.selectbox(
        "Rewrite Style",
        ["Clear and Simple", "Formal", "Casual and Friendly", "Persuasive"]
    )
 


button=st.button('Generate')

if button:

   result = llm(task, user_input, target_language=target_language)
   st.write(result)
else:
    pass