# Chemin vers le fichier de données.
data_file = "données/MockPatientDatabaseOscar.csv"

# Création du menu :
#   id : identifiant de l'onglet (facultatif).
#   label : Le nom de l'onglet tel qu'il apparaît dans le menu.
#   icon : un emoji ou un faticon visible sur l'onglet dans le menu.
menu = [
    {'label': "Accueil", 'icon': "🏠", 'id': "home"},
    {'label': "Lecture des données", 'icon': "📖", 'id': "data"},
    {'label': "Transformation des données", 'icon': "⚙️", 'id': "transform-data"},
    {'label': "Statistiques descriptives", 'icon': "🧮", 'id': "stats"},
    {'label': "Représentations graphiques des variables", 'icon': "📊", 'id': "variables"},
    {'label': "Probabilités de survie et courbe de survie", 'icon': "📈", 'id': "survie"},
    {'label': "Prédiction de survie d'un individu avec Kaplan-Meier", 'icon': "🔎", 'id': "prédiction_kmf"},
    {'label': "Modèle de régression de Cox", 'icon': "📉", 'id': "régression"},
    {'label': "Prédiction de survie d'un individu avec Cox", 'icon': "🔎", 'id': "prédiction_cox"},
    {'label': "Analyse coût-efficacité", 'icon': "🧐", 'id': "coût-efficacité"}
]

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

filters = {
    "Genre": "Genero",
    "Tranche d'âge": "tranche_age",
    "Indice de Masse Corporelle": "IMC",
    "Assurance maladie": "Regimenafiliacion",
    "Anémie": "Anemia",
    "Fragilité": "Fragilidad",
    "FISH (del17p1)": "FISHdel17p1",
    "Sous-classification par plateforme": "SubclasificacionplataformaMM",
    "ISS par la plateforme": "ISSPlataforma1",
    "Traitement du myélome multiple 1": "TtoMM1",
    "Traitement du myélome multiple 2": "TtoMM2",
}

list_filters = list(filters.keys())

# Création d'une liste d'option pour le menu dans les probabilités de survie et courbe de survie avec Kaplan-Meier
options_survie = {
    "1 - Tableaux : Proportions de survivants et intervalles de confiance ": "array",
    "2 - Courbe de survie et intervalles": "global_curve_trust",
    "3 - courbe de survie par genre": "curve_by_genre",
    "4 - courbe de survie par genre avec intervalle de confiance": "curve_by_genre_trust"
}
list_options_survie_label = list(options_survie.keys())

# Création d'une liste de colonnes pour créer les colonnes à choisir pour le modèle de régression de Cox
# clé: valeur
# [nom compréhensible]: [nom de la colonne]
option_cox_model = {
    "Genre": "Genero",
    "Assurance maladie": "Regimenafiliacion",
    "Anémie": "Anemia",
    "Hypercalcémie": "Hipercalcemia",
    "Fragilité": "Fragilidad",
    "FISH (del17p1)": "FISHdel17p1",
    "Traitement du myélome multiple 1": "TtoMM1",
    "Traitement du myélome multiple 2": "TtoMM2",
    "Hospitalisation": "hospitalisation",
    "Tranche d'âge": "tranche_age",
}
# Récupération des clé dans une liste.
list_option_cox_model_label = list(option_cox_model.keys())

# Liste d'options pour le menu dans le modèle de régression de Cox
menu_model_cox = {
    "1 - Présentation des paramètres du modèle de régression de Cox": "params",
    "2 - Présentation des p-value du modèle de régression de Cox": "p_value",
    "3 - Présentation des ratios de risques du modèle de régression de Cox": "hazard_ratios",
    "4 - Détails des résultats du modèle de régression de Cox": "summary",
}
list_menu_model_cox_label = list(menu_model_cox.keys())
