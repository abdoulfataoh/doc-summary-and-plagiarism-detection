# coding: utf-8

from isort import stream
from sklearn.utils import column_or_1d
import streamlit


def _get_models_name() -> list:
    return ["Word2vec", "Camembert", "All-Mini-Lm", "Distil-use"]


streamlit.set_page_config(
    page_title="summarizer",
    page_icon="⚡"
)

# sidebar
streamlit.sidebar.header("Settings")
model = streamlit.sidebar.selectbox("Choose model", _get_models_name())
display_metric = streamlit.sidebar.checkbox("Display metrics ?")

# main
streamlit.markdown(
    """
        # Text summarizer
        A text summarizer tool based on deep learning models
        <br>
    """
)
streamlit.write("##")
file = streamlit.text_area("Enter your text here to get a summary", "Entrez du texte ici pour le resumé")
streamlit.write("#")
validate_btn = streamlit.button("summarizer")

if validate_btn:
    streamlit.empty()
    for i in range(10):
        column_one, column_two = streamlit.columns(2)
        column_one.info("Check plagiarism from")
        column_two.warning("similar sentence")
