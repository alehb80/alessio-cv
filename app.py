from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv_alessio_ligios_data_scientist_ita.pdf"
profile_pic = current_dir / "assets" / "alessio_ligios.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Alessio Ligios"
PAGE_ICON = "📌"
NAME = "Alessio Ligios"
DESCRIPTION = """
Data Scientist
"""
EMAIL = "alessio.ligios@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/alessioligios",
    "GitHub": "https://github.com/alehb80",
}
PROJECTS = {    
    "📁 NMT NER - Translations from Latin to English with Deep Learning": "https://github.com/alehb80/nmt_ner",
    "📁 Skin Lesion Classification - ML techniques for skin cancer diagnosis ": "https://github.com/alehb80/skin-lesion-classification",
    "📁 Civitas Procuratio - Web Application for managing groups of people": "https://github.com/alehb80/civitas-procuratio",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" ⬇️ Download CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📬", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"🔗 [{platform}]({link})")


# --- BIO ---
st.write('\n')
st.subheader("PROFILO")
st.write("---")
st.write(
    """
Sono un Data Scientist altamente motivato con esperienza nel campo dell'analisi dei dati e dell’Intelligenza Artificiale. Con un forte background in materie scientifiche e ingegneristiche, ho dimostrato la mia capacità di tradurre dati complessi in soluzioni aziendali concrete. Sono un appassionato risolutore di problemi che si impegna a migliorare continuamente le mie competenze tecniche e a fornire insight basati su dati per guidare le decisioni aziendali.
"""
)


# --- EXPERIENCE ---
st.write('\n')
st.subheader("ESPERIENZE LAVORATIVE")
st.write("---")

# --- JOB 1
st.write("💼", "**Data Scientist**")
st.write("*Live Tech - Amplify your Data*")
st.write("04/2021 - Presente")
st.write(
    """
- ► Implementazione modelli di classificazione contenuti testuali.
- ► Tecniche di NLP per estrarre entità da grandi volumi di dati testuali.
- ► Analisi serie temporali e implementazione modelli predittivi per previsioni future.
- ► Tecniche di NLP per analisi del testo attraverso modelli di embeddings e confronto vettoriale.
- ► Architetture backend a microservizi.
"""
)

# --- JOB 2
st.write('\n')
st.write("💼", "**Sviluppatore Software**")
st.write("*Università degli Studi RomaTre*")
st.write("03/2018 - 07/2020")
st.write(
    """
- ► Analisi, progettazione, sviluppo e testing per la realizzazione di un'applicazione web per un importante ente pubblico.
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("COMPETENZE")
st.write("---")
st.write(
    """
- 👨‍💻 Programming: Python (sklearn, keras, LangChain), SQL.
- 📊 Data Visulization: Matplotlib, Plotly, Streamlit.
- ⚙️ Data Analysis: Pandas, NumPy.
- 🔨 Modeling: Classic ML, Neural Networks, Time Series, LLM, Generative AI.
- 🤖 NLP: NLTK, StanfordNERTagger, spaCy, Neural Machine Translation.
- 🗄️ Databases: Relational DBs, Postgres, NoSQL Data Bases, MongoDB.
- 💾 Operating Systems: Linux, macOS, Windows.

"""
)


# --- EDUCATION ---
st.write('\n')
st.subheader("EDUCAZIONE")
st.write("---")

# --- EDUCATION 1
st.write("📕", "**Laurea Magistrale in Ingegneria Informatica**")
st.write("*Università degli Studi RomaTre*")
st.write(
    """
- ► Votazione: 110/110.
- ► Corsi di specializzazione in ambito Machine Learning e analisi dei Dati.
- ► Tesi: "Riconoscere entità in un corpus in lingua latina non etichettato attraverso Neural Machine Translation".
"""
)

# --- EDUCATION 2
st.write('\n')
st.write("📕", "**Laurea Triennale In Ingegneria Informatica**")
st.write("*Università degli Studi RomaTre*")
st.write(
    """
- ► Votazione: 87/110.
- ► Tesi: "Progettazione di un sistema per la gestione di un complesso di ospiti distribuiti in strutture".
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("PROGETTI")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- Certification & Badge ---
st.write('\n')
st.subheader("CERTIFICAZIONI")
st.write("---")

# --- Certification 1
st.write("🏅", "**IT Service Management**")
st.write("*ITIL 4 Foundation*")
st.write(
    """
- ► Competenze: Gestione servizi IT - Project management.
"""
)

# --- Certification 2
st.write('\n')
st.write("🏅", "**Learning Python**")
st.write("*LinkedIn Learning*")
st.write(
    """
- ► Competenze: Python.
"""
)

# --- Certification 3
st.write('\n')
st.write("🏅", "**Deep Learning with Flux.jl**")
st.write("*Julia Academy*")
st.write(
    """
- ► Competenze: NumPy · Scikit-Learn · Keras · Pandas · Machine learning.
"""
)