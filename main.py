# Import
import streamlit as st
import pandas as pd
# import lifelines
# import plotly.express as px
# import plotly.graph_objects as go
# import matplotlib as plt
import hydralit_components as hc
from random import randint
from typing import Union

# Import files
import constant
import text
import code_text


# Fonctions
# Lecture du fichier de données
def load_data() -> pd.DataFrame:
    """Lis le fichier de données "MockPatientDatabaseOscar.csv" avec l'encodage latin-1"""
    data = pd.read_csv(constant.data_file, sep=";", encoding='latin-1')
    return data


def print_data(data: Union[pd.DataFrame, list]) -> None:
    """
    Créé une checkbox permettant d'afficher ou non les données.
    """
    show_data = st.checkbox(
        label="Montrer les données",
        value=False
    )
    if show_data:
        st.write(data)


def print_code(text: str, key: str, separator: bool = False) -> None:
    """Affiche le texte sous forme de code.\\
    Le paramètre key permet de donner un identifiant à la checkbox pour éviter une erreur qui apparaît lorsque
    plusieurs checkbox n'ont pas de clés et ont la même structure.\\
    Le paramètre separator permet d'afficher une ligne horizontale avant la checkbox pour séparer le code de
    la partie précédente de la page.
    """
    if separator:
        st.write("---")
    show_code = st.checkbox(
        label="Montrer le code",
        value=True,
        key=key
    )
    if show_code:
        st.code(text, 'python')


def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Applique des transformations au données de base data obtenue avec le fichier "MockPatientDatabaseOscar.csv".\\
    Dans l'ordre :
    - Ajout de la variable time2 qui indique le temps avant hospitalisation (0<time2<time).
    - Ajout de la variable hospitalisation qui indique si le patient a été  hospitalisé ou non
    (environ 1/3 oui et 2/3 non).
    - Ajout de la tranche d'âge du patient (< 50 ans, entre 50 ans et 64 ans, 65+).
    """
    # Parcours les lignes du dataFrame
    for i in range(len(data.index)):
        # Créer la variable time2 compris entre [1; time - 1]
        data.loc[i, 'time2'] = randint(1, data.loc[i, 'time']-1)

        # Créer la variable hospitalisation.
        # proba prend une valeur aléatoire entre 1 et 3.
        proba = randint(1, 3)
        # Si strictement plus petite que 2 (1 chance sur 3) alors le patient est hospitalisé.
        if proba < 2:
            data.loc[i, 'hospitalisation'] = True
        # Sinon (2 chances sur 3), le patient n'est pas hospitalisé.
        else:
            data.loc[i, 'hospitalisation'] = False

        # Créer la variable age entre 16 ans (âge légal pour répondre à des questionnaires sans autorisation parentale)
        # et 112 ans (âge de la doyenne française en 2023).
        age = randint(16, 112)
        # En fonction du résultat, le patient fait partie d'une tranche d'âge différente.
        if age < 50:
            data.loc[i, 'tranche_age'] = "Age < 50"
        elif age < 65:
            data.loc[i, 'tranche_age'] = "Age 50 - 64"
        else:
            data.loc[i, 'tranche_age'] = "Age 65+"
    return data


def print_statistiques_descriptives(data: pd.DataFrame) -> None:
    """
    Affiche les statistiques d'une variable choisie parmis une liste d'options.
    """
    choice = st.selectbox(label="Variable :", options=constant.list_option_descriptives_label)
    stats = data[constant.option_descriptives.get(choice)].describe()
    st.write(stats)


def top_menu() -> None:
    """
    Affiche le menu horizontal et également le contenu des pages une fois choisies sur le menu.
    """
    # Configuration du menu
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
        print_code(code_text.load_data, "load_data", True)
    # Affichage des données une fois transformée et explication du code utilisé ainsi que de notre façon de faire.
    if menu == "transform-data":
        "# ⚙️ Transformation des données"
        print_data(data_transform)
        st.write(text.presentation_transformation_title_time2)
        print_code(code_text.code_time2, "time2")
        st.write(text.presentation_transformation_hospitalisation)
        print_code(code_text.code_hospitalisation, "hospital")
        st.write(text.presentation_transformation_tranche_age)
        print_code(code_text.code_tranche_age, "tranche_age")
    # Affichage des statistiques descriptives
    if menu == "stats":
        "# 🧮 Statistiques descriptives"
        print_statistiques_descriptives(data_transform)
        print_code(code_text.code_stats_descriptives, "stats_descriptives", True)
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


def left_menu() -> None:
    """
    Affiche des éléments dans le menu vertical gauche (natif à streamlit).
    """
    st.sidebar.select_slider(
        label="Temps",
        options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )


# Charge les données
data = load_data()
# Charge les données transformées
data_transform = transform_data(data)

# Page web :
top_menu()
left_menu()
