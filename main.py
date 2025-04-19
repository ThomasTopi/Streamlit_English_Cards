import src.streamlit_window as sw
import streamlit as st

def get_motivation_title(num):
    if num <= 10:
        st.write(f"Procvičeno slov: {num}")
    if num >= 11 and num <= 20:
        st.write(f"WOW dobrá práce, procvičeno: {num} slov")
    if num >= 21 and num <= 40:
        st.write(f"Blázen! Už máš procvičeno: {num} slov")
    if num >= 41 and num <=399:
        st.write(f"Brzo budeš jak rodilej mluvčí! Už máš procvičeno: {num} slov")
    if num >= 400:
        st.write(f"Nejspíš už si viděl všchno, řekni si o další slovíčka máš procvičeno: {num} slov")

def main():
    st.image("logo.jpg", use_container_width=True)
    sw.MainGui_English()
    get_motivation_title(sw.MainGui_English.word_counter)
    if st.button("Restart"):
        sw.MainGui_English.word_counter = 0
        st.write("Seasion restarted, click to 'Next one' to reload")

if __name__=="__main__":
    main()