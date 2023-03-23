home = """
# Analyse de survie  
Ce document présente le travail effectué par Maxime Dangelser et Alexis Aulagnier dans le cadre du cours de Projet d’ingénierie des données du Master 1 MIAGE de Polytech Lyon.
Le sujet porte sur l’analyse de survie avec la bibliothèque lifeline en python.
## Présentation du jeu de données :
Nous n’avons pas d’informations sur le jeu de données et nous n’en avons pas trouvé sur internet non plus.
Le jeu de données s’appelle MockPatientDatabaseOscar, « mock patient » voulant dire « faux patient », ce doit être un jeu de données factice représentant une population de personnes en train de se faire soigner.
Le jeu de données contient 52 lignes et nous allons utiliser 3 colonnes :
- Le genre (Homme ou Femme) ~ Genero
- Le temps (entre 10 et 611 qui représente le moment où les données du patient ont été récupérés durant la durée de l’étude) ~ time
- L’évènement (0 : le patient est en vie, 1 : le patient est mort) ~ Evento
## Présentation du langage utilisé :
Lors de ce projet nous avons utilisé le langage de programmation Python.
Python est un langage de programmation interprété, à syntaxe claire et simple, et qui met l'accent sur la lisibilité du code. Il est facile à apprendre et à utiliser pour les débutants en programmation, mais aussi assez puissant pour être utilisé dans des projets complexes.
Python est un langage polyvalent, utilisé dans une grande variété d'applications, notamment pour la science des données, l'apprentissage automatique, la création d'applications web, l'automatisation de tâches, les scripts système, les jeux et bien plus encore.
Il a une grande communauté de développeurs qui ont créé une multitude de bibliothèques et de frameworks, tels que Pandas, Numpy, Matplotlib, Django, Flask, etc., qui facilitent le développement de projets de différentes tailles et complexités.
En outre, Python est un langage open-source, ce qui signifie que tout le monde peut l'utiliser, le modifier et le distribuer librement. C'est un langage très populaire et largement utilisé dans l'industrie, l'éducation et la recherche.
## Présentation des bibliothèques utilisées :
Pour effectuer ce travail nous avons utilisé différentes bibliothèques présentées ci-dessous.
### Pandas :
Pandas est une bibliothèque open-source pour Python qui permet de manipuler et d'analyser des données tabulaires.
Pandas fournit des fonctionnalités pour lire et écrire des données dans différents formats de fichiers, tels que CSV, Excel, JSON, SQL et bien plus encore. Elle permet également de nettoyer et de préparer les données pour l'analyse, notamment en gérant les valeurs manquantes et en effectuant des opérations de fusion, de regroupement et de filtrage.
### LifeLines :
Lifelines est une bibliothèque open-source de Python qui fournit des outils pour l'analyse de données de survie et l'estimation de la durée de vie. Elle est conçue pour les scientifiques des données, les ingénieurs et les chercheurs qui travaillent avec des données de survie dans divers domaines tels que la médecine, l'économie, l'ingénierie, la biologie et bien d'autres encore.
Lifelines permet de modéliser et d'analyser des données de survie à l'aide de techniques telles que l'estimation de la fonction de survie, l'analyse de la durée de vie, les courbes de Kaplan-Meier, les modèles de régression Cox et bien d'autres encore. Elle fournit également des fonctionnalités pour l'analyse des données censurées, telles que les données de survie tronquées, les données de survie avec des valeurs manquantes, les données de survie intervalles et bien d'autres encore.
### Streamlit :
Streamlit est une bibliothèque open-source de Python qui permet de créer facilement des applications web interactives à partir de scripts Python. Elle fournit une interface simple et intuitive pour créer des applications web en utilisant des commandes simples telles que "st.title", "st.write", "st.plot" et bien d'autres encore.
Streamlit permet aux utilisateurs de créer des applications web interactives à partir de scripts Python en quelques minutes, sans avoir à apprendre des langages de programmation web tels que HTML, CSS ou JavaScript. Elle prend également en charge les graphiques interactifs, les cartes, les animations, les widgets, les formulaires et bien d'autres encore.
Streamlit est très populaire dans la communauté des scientifiques des données, car elle permet de créer des tableaux de bord interactifs pour visualiser et explorer des données rapidement et facilement. Elle est également très utile pour la création de prototypes, la démonstration de concepts, la formation et l'enseignement.
### Plotly :
**Plotly** est une bibliothèque de visualisation de données en Python, utilisée pour créer des graphiques interactifs. Elle propose deux interfaces pour créer des graphiques : plotly.express et plotly.graph_objects.
**Plotly.express** est une interface haut niveau pour créer des graphiques rapidement et facilement. Elle est construite sur la base de la bibliothèque pandas et est conçue pour être facile à utiliser pour les débutants en visualisation de données. Elle fournit une grande variété de graphiques prêts à l'emploi pour les types de données les plus courants, tels que les graphiques en barres, les graphiques à secteurs, les graphiques en nuage de points, les diagrammes en boîte, les histogrammes, etc. Il est également possible de personnaliser ces graphiques en ajoutant des options pour la couleur, la taille, les axes, etc.
**Plotly.graph_objects** est une interface bas niveau pour créer des graphiques plus personnalisés. Elle est conçue pour les utilisateurs avancés qui souhaitent un contrôle total sur leur graphique. Cette interface permet de créer des graphiques à partir de zéro en ajoutant des éléments tels que des axes, des titres, des annotations, des légendes, des formes et des images. Elle permet également de créer des graphiques interactifs en ajoutant des événements, des animations et des liens.
### Matplotlib :
Matplotlib est une bibliothèque de visualisation de données en Python qui permet de créer des graphiques statiques. Matplotlib.pyplot, souvent abrégé en plt, est un module de Matplotlib qui fournit une interface de programmation similaire à celle de MATLAB pour créer des graphiques en utilisant des commandes simples.
## Présentation du code :
Le code est trouvable dans les fichiers main.py, constant.py et est commenté.
"""
