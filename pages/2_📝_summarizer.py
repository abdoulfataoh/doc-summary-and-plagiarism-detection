# coding: utf-8

import base64
from uuid import uuid4 as uuid

import streamlit as st
from PIL import Image

from app import settings
from app.models.summarize import BarthezOrange
from app.models.summarize import OpenAi
from app.dataloader import DataLoader
from predict import predict_summary

models = {
    'BarthezOrange': BarthezOrange,
    'OpenAi': OpenAi,
}


st.set_page_config(
    page_title='summary',
    page_icon='📝',
)

st.image(Image.open(r'docs/citadel.png'))

st.markdown(
    'RESUME DE DOCUMENT DE L’ADMINISTRATION'
)

model_name = st.sidebar.selectbox(
    'Choose model',
    list(models.keys())
)

model_class = models[model_name]
if model_name == 'OpenAi':
    model: OpenAi
    model = model_class(
        api_key=settings.OPENAI_API_KEY,
        model_name='text-davinci-003',
    )
else:
    model = model_class()

section_min_words = st.sidebar.slider('Choose threshold', 40, 200, 50)
uploaded_file = st.file_uploader("Upload your document", type=['pdf'])

if uploaded_file is not None:
    operation_id = id = uuid().hex[:8]
    bytes_data = uploaded_file.getvalue()
    name = uploaded_file.name
    file = settings.WORKDIR / f'{operation_id}-{name}'
    with open(file, 'wb') as f:
        f.write(bytes_data)

    dt = DataLoader(
        filespath=file,
    )
  
    progress_text = 'Operation in progress. Please wait....'
    st.title(progress_text)
    progress_bar = st.progress(0)
    predictions = predict_summary(
        model=model,
        doc_dataloader=dt,
        max_tokens=section_min_words,
    )
    for prediction in predictions:
        progress = prediction['progress']
        progress = int(progress)
        progress_bar.progress(progress)

    summarize_document = settings.WORKDIR / f'summary-{operation_id}-{name}'
    with open(summarize_document, 'rb') as f:
        st.download_button(
            label="Download Repport File",
            data=f,
            file_name=summarize_document.name,
            mime='application/pdf',
        )
