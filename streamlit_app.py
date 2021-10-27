import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
from transformers import pipeline

st.image('flags.jpg',use_column_width=True)
st.title('Tłumacz z języka angielskiego na niemiecki')

st.text('Ta aplikacja tłumaczy słowa z języka angielskiego na język niemiecki.')
st.text('Wpisz słowo w języku angielskim a następnie kliknij przycisk \'Tłumacz\'.')

option = st.selectbox(
    "Opcje tłumaczenia",
    [
        "Tłumaczenie z języka angielskiego na niemiecki"
    ],
)
text = st.text_area(label="Wpisz tekst do przetłumaczenia")

if st.button('Tłumacz'):
    if text == "":
        st.error("Podaj słowo do przetłumaczenia")
    else:
        st.spinner()
        with st.spinner(text='Tłumaczę...'):
            translator = pipeline("translation_en_to_de")
            answer = translator(text)[0]["translation_text"]
            st.success(answer)

st.text('s19288')
