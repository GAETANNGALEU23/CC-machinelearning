import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sn

A = pd.read_csv("train.csv") 
#B = pd.read_csv("test.csv") 

# PAGE D'ACCUEIL
st.title("Analyse et Prediction des Prix de Vente d'une Maison")
st.markdown("""Ce Dashboard explore les donnees sur les maisons a AMES, IOWA""")

#Analyse Exploratoire
st.header("Analyse Exploratoire")
st.subheader("Apercu des donnees")
st.write(A.head()) 

#VISUALISATION 
st.subheader("Analyse de correlation")
#corr = train.corr() 
fig, ax = plt.subplots(figsize=(10, 8))
sn.heatmap(corr, annot=False, cmap="coolwarm", ax=ax)
st.pyplot(fig)

#fig, ax = st.subplots()
#st.hisplot(A['SalePrice'], kde=True, ax=ax)
#st.pyplot(fig)





