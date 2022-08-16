# coding: utf-8

import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)


st.image(Image.open(r'pages/logo_citadel.png'))


st.markdown(
    """
    
    ### Deep learning models for plagiarism and text summarization
   
    """
)
