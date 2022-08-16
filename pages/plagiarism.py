# coding: utf-8

import streamlit as st
import base64

from utils import Granularity
from predict import PredictionPlagiarismDetection

def _get_models_name() -> list:
    models = [
        'gensim_doc2vec',
        'distiluse-base-multilingual-cased-v1',
        'all-MiniLM-L6-v2',
        'camembert_large'

    ]
    return models

def make_tmp_file(uploader_file):
    with open(r".streamlit/tmp.pdf", "wb") as file:
        file.write(uploader_file.read())
    return r".streamlit/tmp.pdf"

st.set_page_config(
    page_title="plagiarism",
    page_icon="🌐"
)

# sidebar
st.sidebar.header("Settings")
model = st.sidebar.selectbox("Choose model", _get_models_name())
sensibility = st.sidebar.slider("sensibility", 0, 100, 50)
display_metric = st.sidebar.checkbox("Display metrics ?")

# main
st.markdown(
    """
        # Plagiarism detection
        plagiarism detection in documents based on deep learning models
    """
)
st.write("##")

uploader_file = st.file_uploader("Choose a pdf document", type="pdf")
st.write("#")
validate_btn = st.button("check plagiarism")


# traitement 
if validate_btn:
    # traitement
    p = PredictionPlagiarismDetection(
        model,
        make_tmp_file(uploader_file),
        Granularity.PARAGRAPH
    )
    progress_bar = st.progress(0)

    for progress in p.predict(sensibility/100):
        progress_bar.progress(int(progress))

    new_file = '.streamlit/tmp-plagiarism.pdf'
    with open(new_file, "rb") as file:
        btn = st.download_button(
            label="download the report",
            data=file,
            file_name=new_file,
        )
