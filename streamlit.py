# coding: utf-8

import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

st.image(Image.open(r'docs/citadel.png'))

st.markdown(
    'APPRENTISSAGE PROFOND POUR LE RÉSUMÉ DE DOCUMENTS ET '
    'LA DÉTECTION DE PLAGIATS DANS LES ÉTUDES DE L’ADMINISTRATION'
)
