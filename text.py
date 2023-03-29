home = """
# Analyse de survie

Ce document présente le travail effectué par Maxime Dangelser et Alexis Aulagnier dans le cadre du cours de
Projet d’ingénierie des données du Master 1 MIAGE de Polytech Lyon.\\
Le sujet porte sur l’analyse de survie avec la bibliothèque lifeline en python.

## Présentation du langage utilisé :

Lors de ce projet nous avons utilisé le langage de programmation Python.

Python est un langage de programmation interprété, à syntaxe claire et simple, et qui met l'accent sur la
lisibilité du code. Il est facile à apprendre et à utiliser pour les débutants en programmation,
mais aussi assez puissant pour être utilisé dans des projets complexes.
Python est un langage polyvalent, utilisé dans une grande variété d'applications, notamment pour la science des données,
l'apprentissage automatique, la création d'applications web, l'automatisation de tâches, les scripts système,
les jeux et bien plus encore.
Il a une grande communauté de développeurs qui ont créé une multitude de bibliothèques et de frameworks,
tels que Pandas, Numpy, Matplotlib, Django, Flask, etc., qui facilitent le développement de projets de différentes
tailles et complexités.\\
En outre, Python est un langage open-source, ce qui signifie que tout le monde peut l'utiliser, le modifier et le
distribuer librement. C'est un langage très populaire et largement utilisé dans l'industrie,
l'éducation et la recherche.

## Présentation des bibliothèques utilisées :

Pour effectuer ce travail nous avons utilisé différentes bibliothèques présentées ci-dessous.

### Pandas :

Pandas est une bibliothèque open-source pour Python qui permet de manipuler et d'analyser des données tabulaires.
Pandas fournit des fonctionnalités pour lire et écrire des données dans différents formats de fichiers, tels que CSV,
Excel, JSON, SQL et bien plus encore. Elle permet également de nettoyer et de préparer les données pour l'analyse,
notamment en gérant les valeurs manquantes et en effectuant des opérations de fusion, de regroupement et de filtrage.

### LifeLines :

Lifelines est une bibliothèque open-source de Python qui fournit des outils pour l'analyse de données de survie et
l'estimation de la durée de vie. Elle est conçue pour les scientifiques des données, les ingénieurs et les chercheurs
qui travaillent avec des données de survie dans divers domaines tels que la médecine, l'économie, l'ingénierie,
la biologie et bien d'autres encore.
Lifelines permet de modéliser et d'analyser des données de survie à l'aide de techniques telles que l'estimation de la
fonction de survie, l'analyse de la durée de vie, les courbes de Kaplan-Meier, les modèles de régression Cox et bien
d'autres encore. Elle fournit également des fonctionnalités pour l'analyse des données censurées,
telles que les données de survie tronquées, les données de survie avec des valeurs manquantes, les données de survie
intervalles et bien d'autres encore.

### Streamlit :

Streamlit est une bibliothèque open-source de Python qui permet de créer facilement des applications web interactives
à partir de scripts Python. Elle fournit une interface simple et intuitive pour créer des applications web en utilisant
des commandes simples telles que "st.title", "st.write", "st.plot" et bien d'autres encore.
Streamlit permet aux utilisateurs de créer des applications web interactives à partir de scripts Python en quelques
minutes, sans avoir à apprendre des langages de programmation web tels que HTML, CSS ou JavaScript.
Elle prend également en charge les graphiques interactifs, les cartes, les animations, les widgets, les formulaires et
bien d'autres encore.
Streamlit est très populaire dans la communauté des scientifiques des données, car elle permet de créer des tableaux de
bord interactifs pour visualiser et explorer des données rapidement et facilement. Elle est également très utile pour
la création de prototypes, la démonstration de concepts, la formation et l'enseignement.

### Plotly :

**Plotly** est une bibliothèque de visualisation de données en Python, utilisée pour créer des graphiques interactifs.
Elle propose deux interfaces pour créer des graphiques : plotly.express et plotly.graph_objects.

**Plotly.express** est une interface haut niveau pour créer des graphiques rapidement et facilement.
Elle est construite sur la base de la bibliothèque pandas et est conçue pour être facile à utiliser pour les débutants
en visualisation de données. Elle fournit une grande variété de graphiques prêts à l'emploi pour les types de données
les plus courants, tels que les graphiques en barres, les graphiques à secteurs, les graphiques en nuage de points,
les diagrammes en boîte, les histogrammes, etc. Il est également possible de personnaliser ces graphiques en ajoutant
des options pour la couleur, la taille, les axes, etc.

**Plotly.graph_objects** est une interface bas niveau pour créer des graphiques plus personnalisés.
Elle est conçue pour les utilisateurs avancés qui souhaitent un contrôle total sur leur graphique.
Cette interface permet de créer des graphiques à partir de zéro en ajoutant des éléments tels que des axes, des titres,
des annotations, des légendes, des formes et des images. Elle permet également de créer des graphiques interactifs en
ajoutant des événements, des animations et des liens.

### Matplotlib :

Matplotlib est une bibliothèque de visualisation de données en Python qui permet de créer des graphiques statiques.
Matplotlib.pyplot, souvent abrégé en plt, est un module de Matplotlib qui fournit une interface de programmation
similaire à celle de MATLAB pour créer des graphiques en utilisant des commandes simples.

## Présentation du code :

Le code est trouvable dans les fichiers main.py, constant.py et est commenté.\\
Il est également trouvable tout au long de ce site via l'option "Montrer le code".
"""

presentation_data = """
---
## Description des données

Nous n’avons pas d’informations sur le jeu de données et nous n’en avons pas trouvé sur internet non plus.\\
Le jeu de données s’appelle MockPatientDatabaseOscar, « mock patient » voulant dire « faux patient », ce doit être un
jeu de données factice représentant une population de personnes en train de se faire soigner.

### Event :skull_and_crossbones: :

L'événement désigne tout événement significatif survenant au cours du traitement du myélome multiple d'un patient,
tel que la progression de la maladie, l'hospitalisation ou le décès.\\
*Dans le cadre de ce projet, l'événement désigne le décès.*

### Time :hourglass_flowing_sand: :

Le temps fait référence à la durée de divers événements liés au traitement du myélome multiple, tels que le temps
écoulé entre le diagnostic et le début du traitement, la durée du traitement ou le temps écoulé jusqu'à la progression
de la maladie.

### Genero :female_sign:/:male_sign: :

Le genre fait référence aux caractéristiques sociales et culturelles qui définissent ce que signifie être un homme ou
une femme dans une société donnée.

### IMC ⚖️ :

L'indice de masse corporelle (IMC) est une mesure utilisée pour évaluer si une personne a un poids sain par rapport à
sa taille.\\
Il est calculé en divisant le poids d'une personne en kilogrammes par le carré de sa taille en mètres
(IMC = poids / taille^2).

### regimenafiliacion :memo: :

Il s'agit de l'ensemble des règles, exigences et procédures qui établissent les conditions d'adhésion d'une personne
à un système de santé.

### Anemia :drop_of_blood: :

Il s'agit d'un état dans lequel l'organisme ne dispose pas de suffisamment de globules rouges sains pour transporter
l'oxygène vers les tissus de l'organisme.\\
L'anémie peut être causée par divers facteurs, notamment un manque de fer, une carence en vitamine B12 ou en
acide folique, des maladies chroniques, etc.

### Fragilidad :man_in_manual_wheelchair: :

Il s'agit d'un état dans lequel une personne connaît une diminution de sa force musculaire, de sa mobilité et de son
endurance physique.

### FISHdel17p1 :dna: :

FISH signifie Fluorescence In Situ Hybridization, une technique utilisée en biologie moléculaire pour détecter et
localiser des séquences d'ADN spécifiques dans les chromosomes. Del17p1 désigne la délétion de matériel génétique sur
le bras court du chromosome 17, qui est une anomalie génétique fréquemment observée dans certains types de cancer,
notamment la leucémie lymphoïde chronique (LLC). La FISH(del17p1) est un test qui utilise des sondes fluorescentes pour
détecter cette anomalie génétique dans les cellules du sang ou de la moelle osseuse d'un patient.

### subclasificacionplataformaMM :microscope: :

La sous-classification par plate-forme est une façon de classer les différents types de tests moléculaires en fonction
de la technologie ou de la plate-forme utilisée pour effectuer le test.\\
Par exemple, le FISH est un type de test moléculaire qui utilise des sondes fluorescentes pour détecter
des séquences d'ADN spécifiques, tandis que la PCR (réaction en chaîne de la polymérase) est un autre type de
test moléculaire qui amplifie des séquences d'ADN pour les détecter. La sous-classification par plate-forme
peut être utile pour comparer les performances et la sensibilité de différents types de tests moléculaires pour
la détection d'anomalies ou de mutations génétiques spécifiques.

### ISSPlataforma1 :test_tube: :

ISS par la plateforme : ISS signifie International Staging System (système international de stadification), un système
utilisé pour classer le myélome multiple en fonction de divers facteurs cliniques et de laboratoire, tels que les taux
d'albumine sérique et de bêta-2 microglobuline. L'ISS par la plateforme fait référence à l'utilisation d'une plateforme
ou d'une technologie spécifique pour classer les patients atteints de myélome multiple en différents stades selon les
critères de l'ISS.

### tToMM1 :syringe: :

Traitement du myélome multiple 1 :\\
Le traitement du myélome multiple 1 fait référence à la première ligne de traitement
prescrite à un patient atteint de myélome multiple, qui peut inclure la chimiothérapie, l'immunothérapie ou d'autres
traitements.

### tToMM2 :syringe: :

Traitement du myélome multiple 2 :\\
Le traitement du myélome multiple 2 désigne la deuxième ligne de traitement
prescrite à un patient atteint de myélome multiple, généralement après que la première ligne de traitement n'a pas
permis de contrôler la maladie ou a entraîné une progression de la maladie.
"""

presentation_transformation_title_time2 = """
---
## Transformations ajoutées

### Ajout de la variable time2

Nous avons ajouté la variable **time2** qui représente le temps avant hospitalisation. Cette donnée est comprise
aléatoirement entre 1 et la date time - 1.
"""

presentation_transformation_hospitalisation = """

### Ajout de la variable hospitalisation

Nous avons ajouté la variable **hospitalisation** qui indique si le patient a été hospitalisé ou non
(comme pour Evento).
La répartition est d'environ 1/3 hospitalisé et 2/3 non hospitalisé.
"""

presentation_transformation_tranche_age = """

### Ajout de la variable tranche d'âge

Nous avons ajouté la variable **tranche_age** qui donne un âge aléatoire au patient entre 16 ans (âge légal à partir
duquel un enfant peut répondre à un questionnaire sans autorisation parentale) et 112 ans (âge de la doyenne en France
en 2023).
Suivant l'âge qui est donné, le patient fera parti de la tranche d'âge des *moins de 50 ans*, *entre 50 et 64 ans* ou
des *plus de 65 ans*.
"""
