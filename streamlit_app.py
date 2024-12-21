import streamlit as st
import pandas as pd
import numpy as np

A = pd.read_csv(train.csv) 

# PAGE D'ACCUEIL
st.title("Analyse et Prediction des Prix de Vente d'une Maison")
st.markdown("""Ce Dashboard explore les donnees sur les maisons a AMES, IOWA""")

#Analyse Exploratoire
st.header("Analyse Exploratoire")
st.subheader("Apercu des donnees")
st.write(A.head())



