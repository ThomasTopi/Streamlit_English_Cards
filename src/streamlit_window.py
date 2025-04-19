import streamlit as st
from src.english_words import get_english_word, get_czech_word, get_random_number

class MainGui_English:

    ID = get_random_number()
    word_counter = 0

    def __init__(self):
        st.title(get_english_word(MainGui_English.ID))
        if st.button("Translate"):
            st.session_state.show_title = False
            st.title(get_czech_word(MainGui_English.ID))   
        st.button("Next One", on_click=self.get_czech_title)
        if st.button("Read  🔊"):
            self.get_voice_title(MainGui_English.ID)

    def get_czech_title(self):
        st.session_state.show_title = False
        MainGui_English.ID = get_random_number()
        MainGui_English.word_counter += 1

    def get_voice_title(self, ID):
        st.audio(f"voice_database//voice_{ID}.mp3", format="audio/mpeg")