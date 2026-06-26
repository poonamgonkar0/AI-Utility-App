
import streamlit as st

 
def build_prompt(task: str, user_input: str, **kwargs) -> str:
    if task == "Summarize Text":
         crafted_prompt=f"""You are an expert summarizer. Read the following text and produce a concise, clear summary.
 
                 Instructions:
                 - Capture the main ideas and key points
                 - Use bullet points for clarity
                 - Keep it under 150 words unless the source is very long
                 - Do not add opinions or external information
 
                 Text to summarize:
                 
                 {user_input}
                 \"\"\"
 
                 Summary:"""
         return crafted_prompt
 
    elif task == "Translate Text":
        target_lang = kwargs.get("target_language")
        crafted_prompt=f"""You are a professional translator. Translate the following text into {target_lang}.
 
                    Instructions:
                    - Preserve the original meaning and tone
                    - Use natural, fluent phrasing in {target_lang}
                    - Do not add explanations — only the translation
 
                    Text to translate:
                    \"\"\"
                    {user_input}
                    \"\"\"
 
                    Translation in {target_lang}:"""
        return crafted_prompt
 
    elif task == "Explain Topic":
        crafted_prompt=f"""You are a skilled professor who can explain complex topics simply.
 
                    Instructions:
                    - Explain the topic clearly for a curious beginner
                    - Use an analogy if helpful
                    - Break it into short paragraphs
                    - Avoid unnecessary jargon
 
                    Topic: {user_input}
 
                    Explanation:"""
        return crafted_prompt
 
    elif task == "Generate Email":
        tone = kwargs.get("email_tone", "Professional")
        crafted_prompt=f"""You are an expert business writer. Write a complete email based on the brief below.
 
                  Tone: {tone}
                  Instructions:
                  - Include: Subject line, greeting, body, and sign-off
                  - Be concise and purposeful
                  - Match the tone specified above
 
                  Brief:
                  \"\"\"
                  {user_input}
                  \"\"\"
 
                  Email:"""
        return crafted_prompt
 
    elif task == "Rewrite Content":
        style = kwargs.get("rewrite_style", "Clear and concise")
        crafted_prompt= f"""You are a professional editor. Rewrite the following content in the specified style.
 
              Target style: {style}
              Instructions:
              - Improve clarity, flow, and readability
              - Keep the original meaning intact
              - Do not add new facts
 
              Original content:
              \"\"\"
              {user_input}
              \"\"\"
 
              Rewritten version:"""
        return crafted_prompt
 
    return crafted_prompt
                