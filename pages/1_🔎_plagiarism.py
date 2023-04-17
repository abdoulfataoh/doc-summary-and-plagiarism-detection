# coding: utf-8

import time
import base64
from uuid import uuid4 as uuid

import streamlit as st
from PIL import Image

from app import settings
from app.models.plagiarism import AllMiniLML6V2
from app.models.plagiarism import DistiluseBaseMultilingualV1
from app.models.plagiarism import Doc2vec
from app.models.plagiarism import CamembertLarge
from app.dataloader import DataLoader
from app import cleaner
from predict import predict_plagiarism

MAX_WAIT_TIME = 10

models = {
    'AllMiniLML6V2': AllMiniLML6V2,
    'DistiluseBaseMultilingualV1': DistiluseBaseMultilingualV1,
    'Doc2vec': Doc2vec,
    'CamembertLarge': CamembertLarge,
}


st.set_page_config(
    page_title='plagiarism',
    page_icon='🔎',
    layout='wide'
)


st.image(Image.open(r'docs/citadel.png'))


st.markdown(
    'DÉTECTION DE PLAGIATS DANS LES ÉTUDES DE L’ADMINISTRATION'
)
model_name = st.sidebar.selectbox(
    'Choose model',
    list(models.keys())
)

model_class = models[model_name]
model = model_class() if model_name != 'Doc2vec' else model_class(
        load_from=str(settings.MODELS_FOLDER / f'model-{model_name}.pickle')
    )

database = settings.EMBEDDINGS_FOLDER / f'emdedings-{model}.pickle'

threshold = st.sidebar.slider('Choose threshold', 0, 100, 70)

max_output = st.sidebar.radio(
    'Max output',
    (1, 2, 3, 'full')
)

uploaded_file = st.file_uploader("Upload your document", type=['pdf'])
file = None
if uploaded_file is not None:
    operation_id = id = uuid().hex[:8]
    bytes_data = uploaded_file.getvalue()
    name = uploaded_file.name
    file = settings.WORKDIR / f'{operation_id}-{name}'

    with open(file, 'wb') as f:
        f.write(bytes_data)

        dt = DataLoader(
            filespath=file,
            cleaner=cleaner,
        )

        tab1, tab2 = st.tabs(['progress bar', 'details'])
        progress_text = 'Operation in progress. Please wait....'
        tab1.subheader(progress_text)
        tab2.subheader('Details')

        progress_bar = tab1.progress(0)

        max_output = max_output if max_output != 'full' else 1000

        tab1_col1, tab1_col2, tab1_col3 = tab1.columns([8, 4, 4])
        tab2_col1, tab2_col2 = tab2.columns([3, 3])

        annoted_document = settings.WORKDIR / f'checked-{operation_id}-{name}'

        predictions = predict_plagiarism(
            model=model,
            database_path=database,
            doc_dataloader=dt,
            threshold=threshold,
            max_output=max_output,
        )

        for prediction in predictions:
            progress = prediction['progress']
            progress_bar.progress(progress)
            for similarity in prediction['similarities']:
                similarity_rate = similarity['similarity_rate']
                similarity_text = similarity['text']
                similarity_filename = similarity['filename']
                similarity_display = f'{similarity_rate}\n{similarity_text}'
                expander = tab2_col2.expander(
                    f'{similarity_rate=} {similarity_filename=}'
                )
                expander.write(similarity_text)

        sleep_time = 1
        while True:
            try:
                with open(annoted_document, 'rb') as f:
                    tab2_col1.write(
                        f'<embed src="data:application/pdf;base64, \
                            {base64.b64encode(f.read()).decode("utf-8")}" \
                                width="650" height="600" \
                                type="application/pdf">',
                        unsafe_allow_html=True,
                    )
                break
            except FileNotFoundError:
                sleep_time = sleep_time + 2
                if sleep_time < MAX_WAIT_TIME:
                    time.sleep(sleep_time)

    # with open(annoted_document, 'rb') as f:
    #     # col2.download_button(
    #     #     label="Download Annoted File",
    #     #     data=f,
    #     #     file_name=annoted_document.name,
    #     #     mime='application/pdf',
    #     # )

    # with open(annoted_document, 'rb') as f:
    #     col3.download_button(
    #         label="Download Repport File",
    #         data=f,
    #         file_name=annoted_document.name,
    #         mime='application/pdf',
    #     )
