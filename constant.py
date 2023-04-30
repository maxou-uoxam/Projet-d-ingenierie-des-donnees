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
    {'label': "Prédiction de survie d'un individu", 'icon': "🔎", 'id': "prédiction"},
    {'label': "Modèle de régression de Cox", 'icon': "📉", 'id': "régression"},
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
