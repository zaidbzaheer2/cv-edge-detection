import streamlit as st
from pages.upload import upload_screen
from pages.detection import  detection_screen
from styles import main_page_style

st.markdown(main_page_style, unsafe_allow_html=True)

st.set_page_config(
    page_title = "Edge Detection",
    layout="wide"
)

if 'uploaded_file' in st.session_state:
    detection_screen()
else:
    upload_screen()