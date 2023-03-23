# Import
import streamlit as st
import pandas as pd
import lifelines
import plotly.express as px
import plotly.graph_objects as go
import matplotlib as plt
from streamlit_option_menu import option_menu
import hydralit_components as hc

# Import files
import constant
import text


# Fonctions
# Lecture du fichier de données
def load_data():
    data = pd.read_csv("données/MockPatientDatabaseOscar.csv", sep=";", encoding='latin-1')
    return data


def print_data():
    show_data = st.checkbox(
        label="Montrer les données",
        value=False
    )
    if show_data:
        st.write(data)


def top_menu():
    st.set_page_config(layout='wide', initial_sidebar_state='collapsed',)
    menu = hc.nav_bar(
        menu_definition=constant.menu,
        hide_streamlit_markers=True
    )

    # Affichage de la page d'accueil avec la présentation du sujet, des données, de python et des librairies utilisées.
    if menu == "home":
        "# 🏠 Accueil"
        st.write(text.home)
    
    # Affichage de la page de présentation des données (visualisation et explication)
    if menu == "data":
        "# 📖 Lecture des données"
        print_data()
    
    # Affichage des données une fois transformée et explication du code utilisé ainsi que de notre façon de faire.
    if menu == "transform-data":
        "# ⚙️ Transformation des données"
    
    # Affichage des statistiques descriptives
    if menu == "stats":
        "# 🧮 Statistiques descriptives"

    # Affichage des variables telles que demandées dans le sujet.
    if menu == "variables":
        "# 📊 Représentations graphiques des variables"
    
    # Affichage des probabilités de survie et des courbes de survie.
    if menu == "survie":
        "# 📈 Probabilités de survie et courbes de survie"
    
    # Affichage des prédictions.
    if menu == "prédiction":
        "# 🔎 Prédiction de survie d'un individu"

    # Affichage de la régression de Cox.
    if menu == "régression":
        "# 📉 Modèle de régression de Cox"
    
    # Affichage de l'analyse coût-efficacité.
    if menu == "coût-efficacité":
        "# 🔎 Analyse coût-efficacité"


def left_menu():
    st.sidebar.select_slider(
        label="Temps",
        options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )


data = load_data()



# Page web :
top_menu()
left_menu()
