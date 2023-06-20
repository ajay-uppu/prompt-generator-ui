import streamlit as st

# Set up Streamlit configuration
st.set_page_config(
    page_title="Prompt Generator",
    page_icon=":bar_chart:",
    layout="wide"
)

# Define CSS styles
main_bg = "background-color: #f0f5f9;"
sidebar_bg = "background-color: #192b3b;"

# Apply CSS styles
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    body {{
        font-family: 'Roboto', sans-serif;
    }}

    .reportview-container {{
        {main_bg}
    }}

    .sidebar .sidebar-content {{
        {sidebar_bg}
    }}

    .css-1p3jvgu, .css-dq8hqf, .css-1n2y7ln {{
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
        padding: 10px;
    }}

    .css-1p3jvgu {{
        background-color: #f0f5f9;
        color: #000000;
    }}

    .css-dq8hqf {{
        background-color: #ffddc1;
        color: #192b3b;
    }}

    .css-1n2y7ln {{
        background-color: #192b3b;
        color: #ffffff;
    }}

    .stButton button:first-child {{
        border-radius: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Create dictionary to store session state
session_state = {}

# Dataset Upload Section
st.header("Dataset Upload")
uploaded_file = st.file_uploader("Upload Dataset", type=["csv", "txt"])

# Persona and Prompt Input Section
col1, col2 = st.columns(2)

with col1:
    st.header("Persona Input")
    if "persona_text" not in session_state:
        session_state["persona_text"] = ""
    Persona = st.text_area("Persona", session_state["persona_text"])
    button_col1, button_col2 = st.columns(2)
    if button_col1.button("Submit"):
        # Store the input text in the session state dictionary
        session_state["persona_text"] = Persona
    if button_col2.button("Clear"):
        # Clear the input text by resetting the value in the session state dictionary
        session_state["persona_text"] = ""
        Persona = ""

with col2:
    st.header("Prompt Output")
    prompt = st.text_area("Prompt")
