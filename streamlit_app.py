import streamlit as st
import pandas as pd
import numpy as np
import altair as alt 
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

#les 05 premieres lignes de notre tableau
st.write(A.head())

#creer un char Altair
chart = alt.Chart(A).mark_bar().encode( x='YrSold' , y='SalePrice')

#Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True)

#creer un char Altair
st.write("FENCE")
chart = alt.Chart(A).mark_bar().encode( x='Fence' , y='SalePrice')

st.write("POOLQC")
chart = alt.Chart(A).mark_point().encode(x='PoolQC' , y='SalePrice')

st.write("LotFrange")
chart = alt.Chart(A).mark_point().encode(x='LotFrontage' , y='SalePrice')

#Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True) 


with st.sidebar:
 #st.title('fonctionalites Prix de Vente d'une Maison') 
   #st.sidebar.subheader("differentes fonctionnalites de notre DASHBOARD :")


 
 #texte d'entree
 st.sidebar.text_input("entrer une valeur") 

#pour le curseur
iris = st.sidebar.slider("MSSubClass:", 50, 10, 300000) 
st.write(f"Vous avez selectionne: {iris} ")

#pour selectionner les cases
with st.sidebar.container():
 st.write("Section 1")
 st.radio("Choix :", ["LotShape","YrSold","LotShape","LandContour","SalePrice"])

#selecteur de liste
#st.sidebar.selectbox("SalePrice:", 18, 100, 25) 
st.sidebar.multiselect("Choix:", ["LotShape","MSZoning","LotShape","LandContour","SalePrice","SaleType"])








