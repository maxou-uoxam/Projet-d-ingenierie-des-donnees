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
