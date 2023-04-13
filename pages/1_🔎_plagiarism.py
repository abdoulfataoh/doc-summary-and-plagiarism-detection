# coding: utf-8

from uuid import uuid4 as uuid

import streamlit as st
from PIL import Image

from app import settings
from app.settings import Granularity as G
from app.models.plagiarism import AllMiniLML6V2
from app.models.plagiarism import DistiluseBaseMultilingualV1
from app.models.plagiarism import Doc2vec
from app.models.plagiarism import CamembertLarge

operation_id = id = uuid().hex[:8]

models = {
    'AllMiniLML6V2': AllMiniLML6V2,
    'DistiluseBaseMultilingualV1': DistiluseBaseMultilingualV1,
    'Doc2vec': Doc2vec,
    'CamembertLarge': CamembertLarge,
}
    

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)


st.image(Image.open(r'docs/citadel.png'))


st.markdown(
    'DÉTECTION DE PLAGIATS DANS LES ÉTUDES DE L’ADMINISTRATION'
)
   
model = st.sidebar.selectbox(
    'Choose model',
    list(models.keys())
)

threshold = st.sidebar.slider('Choose threshold', 0, 100, 70)

uploaded_file = st.file_uploader("Upload your document", type=['pdf'])
file = None
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    name = uploaded_file.name
    file = settings.WORKDIR / f'{operation_id}-{name}'
    with open(file, 'wb') as f:
        f.write(bytes_data)
        tab1, tab2 = st.tabs(['progress bar', 'details'])

        progress_text = 'Operation in progress. Please wait....'
        tab1.subheader(progress_text)
        progress_bar = tab1.progress(0)
        progress_bar.progress(50)
        tab1.download_button(
            label="Download the repport",
            data='csv',
            file_name='large_df.csv',
            mime='application/pdf',
        )

        tab2.subheader('Details')
