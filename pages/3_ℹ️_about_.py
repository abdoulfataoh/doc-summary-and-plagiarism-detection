# coding: utf-8

from uuid import uuid4 as uuid

import streamlit as st
from PIL import Image
  

st.set_page_config(
    page_title="About",
    page_icon='ℹ',
)


st.image(Image.open(r'docs/citadel.png'))


st.markdown(
    'DÉTECTION DE PLAGIATS DANS LES ÉTUDES DE L’ADMINISTRATION'
)

st.title('')

st.markdown(
    '### abdoulfataoh, projet de stage de master'
)
