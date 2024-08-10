import streamlit as st


intro_page = st.Page("Intro.py", title="Introdução", icon="📑")
part_1 = st.Page("Parte1.py", title="Parte 1", icon="1️⃣")
part_2 = st.Page("Parte2.py", title="Parte 2", icon="2️⃣")

pg = st.navigation([intro_page, part_1, part_2])

st.set_page_config(
        page_title="Intro",
        page_icon="Infnet_logo.png",
        layout="wide",
        initial_sidebar_state = "expanded")

pg.run()
