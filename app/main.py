import os
import sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from google.adk.runners import InMemoryRunner
from google.genai.types import Content, Part
from agents.agent import root_agent
import PIL.Image

# runner initialization
runner = InMemoryRunner(agent=root_agent)

# page configuration & styling
st.set_page_config(page_title="Nusantara Trade Sentinel", page_icon="🛰️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { background-color: #006738; color: white; border-radius: 5px; }
    .stTextInput>div>div>input { background-color: #1a1c24; color: white; }
    </style>
    """, unsafe_allow_html=True)

# sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/66/Flag_of_Malaysia.svg", width=100)
    st.title("🛰️ Sentinel Control")
    st.info("Status: **Active**\n\nConnected to: **BNM / MIDA / BigQuery**")
    st.divider()
    st.caption("Monitoring: GDP, CPI, and Trade Balance (Real-time)")

# main interface
st.title("🛰️ Nusantara Trade Sentinel")
st.subheader("Cross-Border Economic Intelligence & Policy Analysis")

# chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# file upload (for chart demo)
uploaded_file = st.file_uploader("Upload Trade Visualization", type=['png', 'jpg', 'jpeg'])

if prompt := st.chat_input("Ask the Sentinel about Malaysia's economy..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        # 1. Prepare the content parts (Text + Image) using explicit keywords
        parts = [Part(text=prompt)]
    
        if uploaded_file:
            image_bytes = uploaded_file.getvalue()
            # Determine mime type dynamically or stick to a safe default
            mime_type = uploaded_file.type 
            parts.append(Part(
                inline_data={
                    "data": image_bytes,
                    "mime_type": mime_type
                }
            ))

        # 2. Wrap in a Content object
        user_message = Content(role="user", parts=parts)

        # 3. Call the runner
        event_stream = runner.run(
            user_id="demo_user",
            session_id="demo_session",
            new_message=user_message
        )

        for event in event_stream:
            if hasattr(event, 'text') and event.text:
                full_response += event.text
                response_placeholder.markdown(full_response + "▌")
        
        response_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})