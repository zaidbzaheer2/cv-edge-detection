import streamlit as st

def upload_screen():
    st.title("Upload Image")
    uploaded_file = st.file_uploader("Choose image", type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        st.session_state.uploaded_file = uploaded_file
        st.rerun()
