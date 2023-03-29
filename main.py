# Import
import streamlit as st
import pandas as pd
import lifelines
import plotly.express as px
import plotly.graph_objects as go
import matplotlib as plt
from streamlit_option_menu import option_menu
import hydralit_components as hc
from random import randint

# Import files
import constant
import text
import code_text


# Fonctions
# Lecture du fichier de données
def load_data():
    data = pd.read_csv("données/MockPatientDatabaseOscar.csv", sep=";", encoding='latin-1')
    return data


def print_data(data):
    show_data = st.checkbox(
        label="Montrer les données",
        value=False
    )
    if show_data:
        st.write(data)


def print_code(text, key):
    show_code = st.checkbox(
        label="Montrer le code",
        value=True,
        key=key
    )
    if show_code:
        st.code(text, 'python')


def transform_data(data):
    for i in range(len(data.index)):
        data.loc[i, 'time2'] = data.loc[i, 'time'] - randint(1, data.loc[i, 'time']-1)
        x = randint(1, 9)
        if x < 3:
            data.loc[i, 'hospitalisation'] = True
        else:
            data.loc[i, 'hospitalisation'] = False
        age = randint(16, 102)
        if age < 50:
            data.loc[i, 'tranche_age'] = "Age < 50"
        elif age < 65:
            data.loc[i, 'tranche_age'] = "Age 50 - 64"
        else:
            data.loc[i, 'tranche_age'] = "Age 65+"
    return data


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
        print_data(data)
        st.write(text.presentation_data)
    
    # Affichage des données une fois transformée et explication du code utilisé ainsi que de notre façon de faire.
    if menu == "transform-data":
        "# ⚙️ Transformation des données"
        print_data(data_transform)
        st.write(text.presentation_transformation_title_time2)
        print_code(code_text.code_time2, "time2")
        st.write(text.presentation_transformation_hospitalisation)
        print_code(code_text.code_hospitalisation, "hospital")
        st.write(text.presentation_transformation_tranche_age)
    
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
data_transform = transform_data(data)

# Page web :
top_menu()
left_menu()
