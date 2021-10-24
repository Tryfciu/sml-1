import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.image('flags.jpg',use_column_width=True)
st.title('Tłumacz z języka angielskiego na niemiecki')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

# st.header('Wprowadzenie do zajęć')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

# st.subheader('O Streamlit')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

st.text('Ta aplikacja tłumaczy słowa z języka angielskiego na język niemiecki.')
st.text('Wpisz słowo w języku angielskim a następnie kliknij ctrl+enter')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

# st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
# write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.

# st.code("st.write()", language='python')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

# with st.echo():
#     st.write("Echo")
# możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy

# df = pd.read_csv("cwiczenie_1.csv", sep = ';')
# st.dataframe(df)
# musimy tylko pamiętaćo właściwym określeniu separatora (w tym wypadku to średnik)
# masz problem z otworzeniem pliku? sprawdź w jakim katalogu pracujesz i dodaj tam plik (albo co bardziej korzystne - zmień katalog pracy)
# os.getcwd() # pokaż bieżący katalog
# os.chdir("") # zmiana katalogu

# st.header('Przetwarzanie języka naturalnego')

import streamlit as st
from transformers import pipeline

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
