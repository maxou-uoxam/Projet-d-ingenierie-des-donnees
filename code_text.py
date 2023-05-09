load_data = """
# Lis le fichier de données "MockPatientDatabaseOscar.csv" avec l'encodage latin-1
data = pd.read_csv(constant.data_file, sep=";", encoding='latin-1')
"""

code_time2 = """
# Parcours les lignes du dataFrame
for i in range(len(data.index)):
    # Créer la variable time2 compris entre [1; time - 1]
    data.loc[i, 'time2'] = randint(1, data.loc[i, 'time']-1)
"""

code_hospitalisation = """
# Parcours les lignes du dataFrame
for i in range(len(data.index)):
    # Créer la variable hospitalisation.
    # proba prend une valeur aléatoire entre 1 et 3.
    proba = randint(1, 3)
    # Si strictement plus petite que 2 (1 chance sur 3) alors le patient est hospitalisé.
    if proba < 2:
        data.loc[i, 'hospitalisation'] = True
    # Sinon (2 chances sur 3), le patient n'est pas hospitalisé.
    else:
        data.loc[i, 'hospitalisation'] = False
"""

# Plus utilisé mais je garde au cas où
code_tranche_age = """
# Parcours les lignes du dataFrame
for i in range(len(data.index)):
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
"""

code_stats_descriptives = """
# Création d'une liste de colonnes pour créer les filtres dans l'application.
# clé: valeur
# [nom compréhensible]: [nom de la colonne]
option_descriptives = {
    "Temps": "time",
    "Mortalité": "Evento",
    "Indice de Masse Corporelle": "IMC",
    "Assurance maladie": "Regimenafiliacion",
    "Anémie": "Anemia",
    "Fragilité": "Fragilidad",
    "FISH (del17p1)": "FISHdel17p1",
    "Sous-classification par plateforme": "SubclasificacionplataformaMM",
    "ISS par la plateforme": "ISSPlataforma1",
    "Traitement du myélome multiple 1": "TtoMM1",
    "Traitement du myélome multiple 2": "TtoMM2",
    "Temps avant hospitalisation": "time2",
    "Hospitalisation": "hospitalisation",
    "Tranche d'âge": "tranche_age",
}
# Récupération des clé dans une liste.
list_option_descriptives_label = list(option_descriptives.keys())

# Créer le filtre permettant de choisir la colonne à décrire.
choice = st.selectbox(label="Variable :", options=constant.list_option_descriptives_label)

# Calcul des statistiques de la colonne demandée
stats = data[constant.option_descriptives.get(choice)].describe()

# Affiche le tableau de statistiques
st.write(stats)
"""


représentation_des_variables_1 = """
# Créé un histogramme pour l'ensemble de la population ou par genre.
# - Vert pour l'ensemble de la population (tous les genres).
# - Bleu pour la population masculine.
# - Rouge pour la population féminine.

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
    title="Répartition des patients du genre \\"Homme\\" en fonction du temps",
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
    title="Répartition des patients du genre \\"Femme\\" en fonction de temps",
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
    option = st.selectbox('Afficher l\\'histogramme pour :', ('Population', 'Hommes', 'Femmes'))
    if option == 'Population':
        fig = fig_all_genre
    elif option == 'Hommes':
        fig = fig_men
    else:
        fig = fig_women

# Affichage du graphique
st.plotly_chart(fig)
"""

représentation_des_variables_2 = """
# Créé un histogramme pour la répartition de la population par genre.
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

# Affiche le graphique
st.plotly_chart(fig)
"""

km_estimator = """
# Estimer la probabilité de survie et l'intervalle de confiance en utilisant la fonction Kanplan-Meyer.

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
"""

plot_km_curve = """
# Représente la courbe de survie avec l'intervalle de confiance sous forme graphique.

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
"""

plot_km_curve_by_sex = """
# Représenter la courbe de Kaplan-Meyer pour chacun des deux groupes (H/F).
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
"""

plot_km_curve_by_sex_with_trust_confidence = """
# Représenter la courbe de Kaplan-Meier pour chacun des geux groupes (H/F) avec l'intervalle de confiance.
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
"""

predict_probabilty_to_survive_using_kmf = """
# Renvoie les valeurs de survie pour les individus existant dans les données a un moment voulu.

# Créer un slider pour choisir le temps entre 0 et le maximum.
time = st.slider(
    label="temps pour lequel prédire une probabilité de survie",
    min_value=0,
    max_value=max(data['time']),
)

# Initialise et règle de modèle de Kaplan-Meier
kmf = KaplanMeierFitter()
kmf.fit(data['time'], event_observed=data['Evento'])

# Calcule la probabilité pour le temps choisis
survival_prob = round(kmf.survival_function_at_times(time).iloc[0] * 100, 2)

# Affiche la probabilité pour le temps choisi
st.write(f"La probabilité de survie pour le temps {time} est de : {survival_prob}%")
"""

explain_cph_params = """
# Initilisation du modèle de Cox
cph = CoxPHFitter()

# Ajustement
cph.fit(
    data,
    duration_col='time',
    event_col='Evento',
    formula=formula
)

# Affichage des paramètres du modèle de régression de Cox
st.write(cph.params_)

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
"""

explain_cph_summary_p = """
# Initilisation du modèle de Cox
cph = CoxPHFitter()

# Ajustement
cph.fit(
    data,
    duration_col='time',
    event_col='Evento',
    formula=formula
)

# Affichage des p-value du modèle de Cox.
st.write(cph.summary.p)

# Génération d'explications automatiques :
# Si la p-value est inférieure à 0.05 alors la variables indique une relation significative avec le risque de mort.
for name, p in cph.summary.p.iteritems():
    p_value = round(p, 2)
    if p_value <= 0.05:
        st.write(f"La variable {name} est statistiquement significative avec une p-value de {p_value}, \
                indiquant une relation significative avec le risque de mort.")
"""

explain_cph_hazard_ratios = """
# Initilisation du modèle de Cox
cph = CoxPHFitter()

# Ajustement
cph.fit(
    data,
    duration_col='time',
    event_col='Evento',
    formula=formula
)

# Affiche les ratios de risques
st.write(cph.hazard_ratios_)

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
"""

cph_summary = """
# Initilisation du modèle de Cox
cph = CoxPHFitter()

# Ajustement
cph.fit(
    data,
    duration_col='time',
    event_col='Evento',
    formula=formula
)

# Affichage des détails du résulta du modèle de Cox
st.write(cph.summary)
"""

survival_prediction = """
#----Création et paramétrage du modèle de Cox----#
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

#-----Création d'un individu------#
# Intialisation
new_individual = {}

# Pour chaque colonne choisis par l'utilisateur, si c'est une colonne qualitative
# l'utilisateur a une liste de choix possible créé à partir des donnés.
# Si c'est une colonne quantitative, il peut entrer le nombre qu'il veut.
for column in params:
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

#----Création du graphique de survie avec Plotly----#
fig = px.line()
for i, survival_curve in enumerate(survival_prediction.values.T):
    fig.add_scatter(x=survival_prediction.index, y=survival_curve, name=f'Individu {i+1}')

fig.update_layout(
    title="Prévision de survie",
    xaxis_title="Durée",
    yaxis_title="Probabilité de survie",
    showlegend=True
)

# Affichage du graphique
st.plotly_chart(fig)

#----Affichage sous forme de table----#
# Checkbox pour donner le choix d'afficher ou non les résultats sous forme de table.
show_datatable = st.checkbox(
    label="Montrer les données sous forme de table",
    value=False,
    key="show_datatable_survival_prediction",
)

# Si la checkbox a la valeur True alors on affiche la table.
if show_datatable:
    st.write(survival_prediction)
"""
