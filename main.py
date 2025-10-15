import streamlit as st
from pages.upload import upload_screen
from pages.detection import  detection_screen

st.markdown("""
    <style>
        /* Hide sidebar and its toggle completely */
        [data-testid="stSidebar"] { display: none; }
        [data-testid="collapsedControl"] { display: none; }
    </style>
""", unsafe_allow_html=True
)

st.set_page_config(
    page_title = "Edge Detection"
)

query_params = st.query_params
if 'uploaded' in query_params:
    detection_screen()
else:
    upload_screen()