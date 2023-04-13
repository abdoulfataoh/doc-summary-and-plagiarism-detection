# coding: utf-8

import streamlit as st

from predict import PredictionSummary


def _get_models_name() -> list:
    models = [
        'bart-large-cnn',
        'camembert2camembert_shared',
        'flaubert'
    ]
    return models


st.set_page_config(
    page_title="summarizer",
    page_icon="⚡"
)

# sidebar
st.sidebar.header("Settings")
model = st.sidebar.selectbox("Choose model", _get_models_name())

# main
st.markdown(
    """
        # Text summarizer
        A text summarizer tool based on deep learning models
        <br>
    """
)
st.write("##")
text = st.text_area("Enter your text here to get a summary", "Entrez du texte ici pour le resumé")
st.write("#")
validate_btn = st.button("summarizer")

if validate_btn:
    s = PredictionSummary(
        model,
        text
    )
    result = s.predict()
    st.info(result)
