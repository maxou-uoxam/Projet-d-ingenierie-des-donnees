# Import
import streamlit as st
import hydralit_components as hc
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
from random import randint
from typing import Union

from lifelines import KaplanMeierFitter, CoxPHFitter

# Import files
import constant
import text
import code_text

# Global


# Fonctions
def load_original_data() -> pd.DataFrame:
    """
    Lis le fichier de données "MockPatientDatabaseOscar.csv" avec l'encodage latin-1
    """
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


def print_code(text: str, key: str, separator: bool = False, show_code_by_default: bool = True) -> None:
    """Affiche le texte sous forme de code.\\
    - Le paramètre key permet de donner un identifiant à la checkbox pour éviter une erreur qui apparaît lorsque
    plusieurs checkbox n'ont pas de clés et ont la même structure.\\
    - Le paramètre separator permet d'afficher une ligne horizontale avant la checkbox pour séparer le code de
    la partie précédente de la page. Par défaut, c'est à False.
    - Le paramètre show_code_by_default permet de choisir si le code est montré par défaut au non.
    Par défaut c'est True, donc le code est affiché.
    """
    if separator:
        st.write("---")
    show_code = st.checkbox(
        label="Montrer le code",
        value=show_code_by_default,
        key=key
    )
    if show_code:
        st.code(text, 'python')


def transform_data() -> pd.DataFrame:
    """
    Applique des transformations au données de base data obtenue avec le fichier
    "MockPatientDatabaseOscar - Modified.csv".\\
    Dans l'ordre :
    - Ajout de la variable time2 qui indique le temps avant hospitalisation (0<time2<time).
    - Ajout de la variable hospitalisation qui indique si le patient a été  hospitalisé ou non
    (environ 1/3 oui et 2/3 non).
    """
    # Récupération des données :
    data = pd.read_csv(constant.data_modified_file, sep=";", encoding='latin-1')
    # Renommage colonne
    data.rename(columns={'Tranche d\'âge': 'tranche_age'}, inplace=True)

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
    return data


def print_statistiques_descriptives(data: pd.DataFrame) -> None:
    """
    Affiche les statistiques d'une variable choisie parmis une liste d'options.
    """
    choice = st.selectbox(label="Variable :", options=constant.list_option_descriptives_label)
    stats = data[constant.option_descriptives.get(choice)].describe()
    st.write(stats)


def filtered_data(data: pd.DataFrame, filters: dict) -> pd.DataFrame:
    """
    Filtres les données et les renvoient
    """
    if filters is None:
        return data
    else:

        for filter in filters:
            if filters[filter] != []:
                data = data[data[filter].isin(filters[filter])]
    return data


def plot_hist_for_data_representation(data: pd.DataFrame, filters: dict) -> None:
    """
    Créé un histogramme pour l'ensemble de la population ou par genre.
    - Vert pour l'ensemble de la population (tous les genres).
    - Bleu pour la population masculine.
    - Rouge pour la population féminine.
    """
    # Graphique pour l'ensemble de la population
    fig_all_genre = px.histogram(
        data,  # Données utilisées
        x='time',  # Variable sur l'axe des abscisses, sans indiquer y c'est alors count qui est calculé.
        color_discrete_sequence=['forestgreen'],  # Couleur pour les données
        title="Répartition de l'ensemble des patients en fonction du temps",  # Titre
    )
    # Ajoute une étiquette aux barres de l'histogramme pour afficher les valeurs
    fig_all_genre.update_traces(
        texttemplate='%{y}',  # Permet d'afficher les valeurs de l'axe des ordonnées.
        textposition='auto',  # Placement de l'étiquette automatique sur les barres
    )
    # Graphique pour la population du genre Homme
    fig_men = px.histogram(
        data.loc[data['Genero'] == 'M'],
        x='time',
        color_discrete_sequence=['deepskyblue'],
        title="Répartition des patients du genre \"Homme\" en fonction du temps",
    )
    fig_men.update_traces(
        texttemplate="%{y}",
        textposition='auto',
    )
    # Graphique pour la population du genre "Femme"
    fig_women = px.histogram(
        data.loc[data['Genero'] == 'F'],
        x='time',
        color_discrete_sequence=['indianred'],
        title="Répartition des patients du genre \"Femme\" en fonction de temps",
    )
    fig_women.update_traces(
        texttemplate='%{y}',
        textposition='auto',
    )

    # Affichage du graphique en fonction du choix sur les filtres (Population, Homme ou Femme).
    # Si le champs Genre est filtré dans le menu vertical, alors l'affichage se fait en fonction de ce filtre
    # Sinon, on affiche une selectbox pour proposer le choix entre les filtres.
    if "Genero" in filters:
        genres = filters["Genero"]
        if genres == [] or ("F" in genres and "M" in genres):
            fig = fig_all_genre
        elif "M" in genres:
            fig = fig_men
        else:
            fig = fig_women
    else:
        option = st.selectbox('Afficher l\'histogramme pour :', ('Population', 'Hommes', 'Femmes'))
        if option == 'Population':
            fig = fig_all_genre
        elif option == 'Hommes':
            fig = fig_men
        else:
            fig = fig_women
    st.plotly_chart(fig)


def plot_hist_for_data_representation_2(data: pd.DataFrame, filters: dict) -> None:
    """
    Créé un histogramme pour la répartition de la population par genre.
    """
    fig = px.histogram(
        data,
        x="Genero",
        color_discrete_sequence=['indianred', 'deepskyblue'],
        color='Genero',
        title="Répartition des patients par genre",
    )
    # Ajoute une étiquette sur la barre de l'histogramme pour afficher la valeur
    fig.update_traces(
        texttemplate='%{y}',
        textposition='auto',
    )
    st.plotly_chart(fig)


def km_estimator(data: pd.DataFrame) -> None:
    """
    Estimer la probabilité de survie et l'intervalle de confiance en utilisant la fonction Kanplan-Meyer.
    """
    # Initialisation du modèle de Kaplan-Meier
    kmf = KaplanMeierFitter()

    # Ajustement du modèle
    kmf.fit(data['time'], event_observed=data['Evento'])

    # Récupération des résultats
    surv_prob = kmf.survival_function_
    conf_int = kmf.confidence_interval_survival_function_

    # Affichage des résultats
    st.write('Tableau des proportions de survivants :')
    st.write(surv_prob)
    st.write('Intervalle de confiance :')
    st.write(conf_int)


def plot_km_curve(data: pd.DataFrame) -> None:
    """
    Représente la courbe de survie avec l'intervalle de confiance sous forme graphique.
    """
    # Initialisation du modèle de Kaplan-Meier
    kmf = KaplanMeierFitter()
    # Ajustement du modèle
    kmf.fit(data['time'], event_observed=data['Evento'])

    # Création du graphique
    fig = go.Figure()
    # Ajout de la courbe de survie
    fig.add_trace(
        go.Scatter(
            x=kmf.timeline,
            y=kmf.survival_function_['KM_estimate'],
            mode='lines',
            name='Probabilité de survie'
        )
    )
    # Ajout de la courbe de confiance inférieure
    fig.add_trace(
        go.Scatter(
            x=kmf.timeline,
            y=kmf.confidence_interval_['KM_estimate_lower_0.95'],
            mode='lines',
            line=dict(dash='dash'),
            name='Intervalle de confiance inférieure'
        )
    )
    # Ajout de la courbe de confiance supérieure
    fig.add_trace(
        go.Scatter(
            x=kmf.timeline,
            y=kmf.confidence_interval_['KM_estimate_upper_0.95'],
            mode='lines',
            line=dict(dash='dash'),
            name='Intervalle de confiance supérieure'
        )
    )
    # Ajout du titre du graphique et des axes
    fig.update_layout(
        title='Courbe de Kaplan-Meier',
        xaxis_title='Temps',
        yaxis_title='Probabilité de survie'
    )

    # Affichage du graphique
    st.plotly_chart(fig)


def plot_km_curve_by_sex(data: pd.DataFrame) -> None:
    """
    Représenter la courbe de Kaplan-Meyer pour chacun des deux groupes (H/F).
    """
    # Initialisation du modèle de Kaplan-Meier et du graphique
    kmf = KaplanMeierFitter()
    fig = go.Figure()

    # Ajustement du modèle pour les 2 genre et affichage des courbes de survie
    for name, grouped_df in data.groupby('Genero'):
        kmf.fit(grouped_df['time'], grouped_df['Evento'], label=name)
        fig.add_trace(go.Scatter(x=kmf.timeline, y=kmf.survival_function_[name], mode='lines', name=name))

    # Ajout du titre du graphique et des axes
    fig.update_layout(
        title='Courbe de Kaplan-Meier par groupe',
        xaxis_title='Temps',
        yaxis_title='Probabilité de survie'
    )

    # Affichage du graphique
    st.plotly_chart(fig)


def plot_km_curve_by_sex_with_trust_confidence(data: pd.DataFrame) -> None:
    """
    Représenter la courbe de Kaplan-Meier pour chacun des geux groupes (H/F) avec l'intervalle de confiance.
    """
    # Création du graphique avec matplotlib
    fig, ax = plt.subplots()

    # Initialisation du modèle de Kaplan-Meier
    kmf = KaplanMeierFitter()

    # Aujstement et création des courbes de survie et de confiance pour chaque genre?
    for name, grouped_df in data.groupby('Genero'):
        kmf.fit(grouped_df['time'], grouped_df['Evento'], label=name)
        kmf.plot(ax=ax)

    # Affichage du graphique
    st.pyplot(fig)


def create_new_individu(data: pd.DataFrame, columns: pd.DataFrame) -> pd.DataFrame:
    """
    Créé un nouvel individu par rapport aux données proposées.
    - data : Cela correspond aux données à partir desquels créé le formulaire.
    - columns : Cela correspond aux colonnes qui doivent être utilisé pour créer l'individu.

    Retourne un individu sous forme de dictionnaire.
    """

    # Intialisation
    new_individual = {}

    for column in columns:
        if data[column].dtype == 'object':
            unique_values = data[column].unique()
            selected_value = st.selectbox(
                label=f"Choisissez une valeur pour {column}",
                options=unique_values,
            )
            new_individual[column] = selected_value
        else:
            input_value = st.number_input(
                label=f"Entrez une valeur pour {column}",
            )
            new_individual[column] = input_value
    # Transformation en DataFrame
    new_individual = pd.DataFrame(new_individual, index=[0])
    return new_individual


def predict_probabilty_to_survive_using_kmf(data: pd.DataFrame) -> None:
    """
    Renvoie les valeurs de survie pour les individus existant dans les données a un moment voulu.
    """
    # Créer un slider pour choisir le temps entre 0 et le maximum.
    time = st.slider(
        label="temps pour lequel prédire une probabilité de survie",
        min_value=0,
        max_value=max(data['time']),
    )
    kmf = KaplanMeierFitter()
    kmf.fit(data['time'], event_observed=data['Evento'])
    survival_prob = round(kmf.survival_function_at_times(time).iloc[0] * 100, 2)

    st.write(f"La probabilité de survie pour le temps {time} est de : {survival_prob}%")


def left_menu_choice_for_regression_model() -> list:
    """
    Créé un nouveau choix de colonnes dans le menu latéral pour la régression de Cox.
    Retourne une liste avec les nom de colonnes.
    """
    # Invitation à choisir les colonnes pour la régression de Cox dans le menu latéral
    st.write("Veuillez choisir dans le menu latéral les colonnes à utiliser dans le modèle de Cox.")

    # Séparation par rapport aux filtres précédents.
    st.sidebar.write("---")

    # Ajout des choix pour la régression de Cox dans le menu latéral
    choices = st.sidebar.multiselect(
        label="Choix des colonnes pour le modèle de Cox",
        options=constant.list_option_cox_model_label,
        max_selections=4,
    )

    # Création du string au format "X + Y + Z"
    formula = []
    for choice in choices:
        formula.append(constant.option_cox_model[choice])
    return formula


def explain_cph_params(cph: CoxPHFitter) -> None:
    """
    Affiche les paramètres du modèle de régression de Cox.
    Et propose une explication automatique des paramètres.
    """
    # Affichage des paramètres du modèle de régression de Cox
    st.write(cph.params_)

    # Donne le choix d'afficher les explications
    show_explanation = st.checkbox(
        label="Montrer les explications",
        value=False,
        key="cox_params"
    )

    if show_explanation:
        # Génération d'explications automatiques :
        # Si coef > 0 l'augmentation de la variable indique une augmentation du risque de mort.
        # Sinon, une diminution de la variable indique une diminution du risque de mort.
        for name, coef in cph.params_.iteritems():
            coefficient = round(coef, 2)

            if coefficient > 0:
                interpretation = f"Une augmentation d'une unité de {name} est associée \
                    à une augmentation de {coefficient}% du risque de mort."
            else:
                interpretation = f"Une diminution d'une unité de {name} est associée \
                    à une diminution de {abs(coefficient)}% du risque de mort."
            st.write(interpretation)


def explain_cph_summary_p(cph: CoxPHFitter) -> None:
    """
    Affiche les p-values du modèle de régression de Cox.
    Et propose une explication automatique des p-value.
    """
    # Affichage des p-value du modèle de Cox.
    st.write(cph.summary.p)

    # Choix de montrer les explications
    show_explanation = st.checkbox(
        label="Montrer les explications",
        value=False,
        key="cox_p_value"
    )
    if show_explanation:
        # Génération d'explications automatiques :
        # Si la p-value est inférieure à 0.05 alors la variables indique une relation significative avec le risque de
        # mort.
        for name, p in cph.summary.p.iteritems():
            p_value = round(p, 2)
            if p_value <= 0.05:
                st.write(f"La variable {name} est statistiquement significative avec une p-value de {p_value}, \
                        indiquant une relation significative avec le risque de mort.")


def explain_cph_hazard_ratios(cph: CoxPHFitter) -> None:
    """
    Affiche les ratios de risques estimés.
    Créé une explication automatique de ces ratios.
    """
    # Affiche les ratios de risques
    st.write(cph.hazard_ratios_)

    # Donne le choix d'afficher les explications
    show_explanation = st.checkbox(
        label="Montrer les explications",
        value=False,
        key="cox_hazard_ratios"
    )

    if show_explanation:
        # Génération des explications automatiques :
        # Si le ratio > 1 alors l'augmentation de la variable indique l'augmentation du risque de mort.
        # Si le ratio < 1 alors l'augmentation de la variable indique la diminutin du risque de mort.
        # Sinon (ratio == 1), la variable n'a pas d'effet sur le risque de mort
        for name, hazard_ratio in cph.hazard_ratios_.items():
            interpretation = f"Un hazard ratio de {hazard_ratio:.2f} est associé à la variable {name}."
            if hazard_ratio > 1:
                interpretation += " Une augmentation de cette variable est associée \
                    à une augmentation du risque de mort."
            elif hazard_ratio < 1:
                interpretation += " Une augmentation de cette variable est associée à une diminution du risque de mort."
            else:
                interpretation += " Cette variable n'a pas d'effet sur le risque de mort."
            st.write(interpretation)


def create_cox_model(data: pd.DataFrame) -> Union[CoxPHFitter, list]:
    """
    Créé le modèle de régression de Cox et l'ajuste avant de le retourner lui et les colonnes utilisés.
    """
    # Ajout des options dans le menu latéral et récupération des colonnes au format "X + Y + Z"
    params = left_menu_choice_for_regression_model()
    formula = " + ".join(params)

    # Initilisation du modèle de Cox
    cph = CoxPHFitter()

    # Ajustement
    cph.fit(
        data,
        duration_col='time',
        event_col='Evento',
        formula=formula
    )
    return cph, params


def presentation_regression_model_cox(data: pd.DataFrame) -> None:
    """
    Utilise le modèle de régression de Cox et montre :
    - les paramètres
    - les p-value
    - les hazard-ratios
    - les résultats détaillés
    """
    menu = st.selectbox(
        label="Choisissez un sujet :",
        options=constant.list_menu_model_cox_label
    )
    choice = constant.menu_model_cox[menu]

    try:
        cph, columns = create_cox_model(data)

        # Explication des paramètres :
        if choice == "params":
            explain_cph_params(cph=cph)
            print_code(
                text=code_text.explain_cph_params,
                key="explain_cph_params",
                separator=True,
            )

        # P-value (si <0.05 alors impact significatif)
        if choice == "p_value":
            explain_cph_summary_p(cph=cph)
            print_code(
                text=code_text.explain_cph_summary_p,
                key="explain_cph_summary_p",
                separator=True,
            )

        # Hazard ratios (la plus grande valeur est celle qui a le plus d'impact sur la mort).
        if choice == "hazard_ratios":
            explain_cph_hazard_ratios(cph=cph)
            print_code(
                text=code_text.explain_cph_hazard_ratios,
                key="explain_cph_hazard_ratios",
                separator=True,
            )

        # Résultats détaillés
        if choice == "summary":
            st.write(cph.summary)
            print_code(
                text=code_text.cph_summary,
                key="cph_summary",
                separator=True,
            )
    except Exception:
        st.error(
            body="Un problème a été rencontré avec ces colonnes veuillez \
            choisir d\'autres colonnes dans le menu latéral",
            icon="🚨"
        )


def plot_survival_prediction_with_cox(survival_prediction) -> None:
    # Création du graphique de survie avec Plotly
    fig = px.line()
    for i, survival_curve in enumerate(survival_prediction.values.T):
        fig.add_scatter(x=survival_prediction.index, y=survival_curve, name=f'Individu {i+1}')

    fig.update_layout(
        title="Prévision de survie",
        xaxis_title="Durée",
        yaxis_title="Probabilité de survie",
        showlegend=True
    )

    st.plotly_chart(fig)


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

    # Création des filtres
    filters = left_menu()

    # Filtration des données de base
    data_filtered = filtered_data(data=data, filters=filters)
    # Filtration des données transformées
    data_transform_filtered = filtered_data(data=data_transform, filters=filters)

    # Affichage de la page d'accueil avec la présentation du sujet, des données, de python et des librairies utilisées.
    if menu == "home":
        "# 🏠 Accueil"
        st.write(text.home)
    # Affichage de la page de présentation des données (visualisation et explication)
    if menu == "data":
        "# 📖 Lecture des données"
        print_data(data_filtered)
        st.write(text.presentation_data)
        print_code(code_text.load_data, "load_data", True)
    # Affichage des données une fois transformée et explication du code utilisé ainsi que de notre façon de faire.
    if menu == "transform-data":
        "# ⚙️ Transformation des données"
        print_data(data_transform_filtered)
        st.write(text.presentation_transformation_title_time2)
        print_code(code_text.code_time2, "time2")
        st.write(text.presentation_transformation_hospitalisation)
        print_code(code_text.code_hospitalisation, "hospital")
        st.write(text.presentation_transformation_tranche_age)
    # Affichage des statistiques descriptives
    if menu == "stats":
        "# 🧮 Statistiques descriptives"
        print_statistiques_descriptives(data_transform_filtered)
        print_code(code_text.code_stats_descriptives, "stats_descriptives", True)
    # Affichage des variables telles que demandées dans le sujet.
    if menu == "variables":
        "# 📊 Représentations graphiques des variables"
        # Représentation du nombre de patients en fonction du temps.
        plot_hist_for_data_representation(data=data_transform_filtered, filters=filters)
        print_code(code_text.représentation_des_variables_1, "représentation_variables_1", False, False)

        st.write("---")
        # Représentation du nombre de patients par genre.
        plot_hist_for_data_representation_2(data=data_transform_filtered, filters=filters)
        print_code(code_text.représentation_des_variables_2, "représentation_variables_2", False, False)
    # Affichage des probabilités de survie et des courbes de survie.
    if menu == "survie":
        # Affichage des proposition de visualisations
        "# 📈 Probabilités de survie et courbes de survie"
        label_options = st.selectbox(
            label="Sélectionner un sujet",
            options=constant.list_options_survie_label
        )
        option = constant.options_survie[label_options]
        # Affichage sous forme de tableau des proportions de survivants dans le temps
        # et des intervalles de confiances.
        if option == "array":
            km_estimator(data=data_transform_filtered)
            print_code(
                text=code_text.km_estimator,
                key="km_estimator",
                separator=True,
            )
        # Affichage de la courbe de survie globale avec les intervalles de confiance
        if option == "global_curve_trust":
            plot_km_curve(data=data_transform_filtered)
            print_code(
                text=code_text.plot_km_curve,
                key="plot_km_curve",
                separator=True,
            )
        # Affichage de la courbe de survie pour chaque genre
        if option == "curve_by_genre":
            plot_km_curve_by_sex(data=data_transform_filtered)
            print_code(
                text=code_text.plot_km_curve_by_sex,
                key="plot_km_curve_by_sex",
                separator=True,
            )
        # Affichage de la courbe de survie pour chaque genre et avec l'intervalle de confiance
        if option == "curve_by_genre_trust":
            plot_km_curve_by_sex_with_trust_confidence(data=data_transform_filtered)
            print_code(
                text=code_text.plot_km_curve_by_sex_with_trust_confidence,
                key="plot_km_curve_by_sex_with_trust_confidence",
                separator=True,
            )
    # Affichage des prédictions avec le modèle de Kaplan-Meier
    if menu == "prédiction_kmf":
        "# 🔎 Prédiction de survie d'un individu avec le modèle de Kaplan-Meier"
        predict_probabilty_to_survive_using_kmf(data=data_transform_filtered)
        print_code(
            text=code_text.predict_probabilty_to_survive_using_kmf,
            key="predict_probabilty_to_survive_using_kmf",
            separator=True,
        )
    # Affichage de la régression de Cox.
    if menu == "régression":
        "# 📉 Modèle de régression de Cox"
        presentation_regression_model_cox(data=data_transform_filtered)
    # Affichage de la prédiction avec le modèle de Cox
    if menu == "prédiction_cox":
        "# 🔎 Prédiction de survie d'un individu avec le modèle de Cox"
        # Création du modèle de régression de Cox et des colonnes ayant été utilisées.
        try:
            cph, choices = create_cox_model(data=data_transform_filtered)
            # Création d'un nouvel individu pour lequel on veut prédire la survie
            new_individual = create_new_individu(data=data_transform_filtered, columns=choices)

            # Prédiction de la survie pour le nouvel individu
            survival_prediction = cph.predict_survival_function(new_individual)

            # Création du graphique de survie avec plotly
            plot_survival_prediction_with_cox(survival_prediction)

            # Afficher les données sous forme de tableau
            show_datatable = st.checkbox(
                label="Montrer les données sous forme de table",
                value=False,
                key="show_datatable_survival_prediction",
            )
            if show_datatable:
                st.write(survival_prediction)
        except Exception as e:
            st.error(
                body=f"Un problème a été rencontré avec ces colonnes veuillez \
                choisir d\'autres colonnes dans le menu latéral {e}",
                icon="🚨"
            )

        print_code(
            text=code_text.survival_prediction,
            key="survival_prediction",
            separator=True
        )
    # Affichage de l'analyse coût-efficacité.
    if menu == "coût-efficacité":
        "# 🔎 Analyse coût-efficacité"
        "Cette partie n'a pas été traitée et n'est plus à faire."


def left_menu() -> dict:
    """
    Affiche des éléments dans le menu vertical gauche (natif à streamlit).
    Propose les colonnes à filtrer en 2 onglets.
    """
    filters = {}
    tab1, tab2 = st.sidebar.tabs(["Choix des colonnes à filrer", "Filtres"])

    with tab1:
        choices = st.multiselect(
            label="Colonnes :",
            options=constant.list_filters,
        )
    with tab2:
        if choices == []:
            st.write("Veuillez choisir des colonnes à filtrer auparavant.")
        else:
            for choice in choices:
                filters[constant.filters.get(choice)] = st.multiselect(
                    label=choice,
                    options=np.unique(data_transform[constant.filters.get(choice)])
                )
    return filters


# Charge les données
data = load_original_data()
# Charge les données transformées
data_transform = transform_data()

# Page web :
top_menu()
