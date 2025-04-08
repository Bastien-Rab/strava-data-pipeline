# 🏃‍♂️ Analyse de la Performance Sportive via un Pipeline de Données Strava

Ce projet personnel a pour objectif de construire un pipeline de données **moderne et automatisé** à partir de mes activités **Strava** (course et vélo). Grâce à une architecture ELT inspirée du monde professionnel, j’analyse l’évolution de ma **condition physique** au fil des années.

---

## 📚 Contexte du Projet

Passionné de course à pied et de data, j’ai voulu créer un projet mêlant **données personnelles et stack data moderne**. À partir de mes propres activités Strava :

- Je construis un pipeline **complet** : extraction via API, stockage PostgreSQL, transformation DBT.
- J'exploite ensuite les données dans un **notebook Python** pour produire des analyses visuelles et statistiques.
- L’objectif est de **mesurer mes progrès** et mieux comprendre les impacts de l'entraînement dans le temps (fréquence cardiaque, vitesse, volume…).

Ce projet simule **une situation réelle d’entreprise**, tout en produisant un livrable personnel, visuel et actionnable.

---

## 🎯 Objectifs du Projet

- 🔌 **Connecter à l’API Strava** pour récupérer les activités (run, ride, etc.).
- 🗄️ **Stocker les données dans PostgreSQL** en format brut.
- 🔧 **Transformer et modéliser les données avec DBT** pour construire des tables d’analyse (staging + marts).
- 📊 **Analyser les métriques sportives clés** :
  - Distance parcourue
  - Évolution de la fréquence cardiaque
  - Corrélation FC / vitesse
  - Saisonnalité de l’effort
  - Tendances de performance
- 💡 Dégager des **insights concrets sur la progression** dans le temps (2019 → 2025).

---

## 📦 Livrables

- ✅ Pipeline ELT complet : API → PostgreSQL → DBT
- 📈 Analyses dans un notebook Jupyter :
  - Statistiques annuelles
  - Moyennes mobiles, LOWESS
  - Corrélations (Pearson / Spearman)
  - Visualisations (Seaborn, Matplotlib)
- 🖼️ Graphiques, slides, et visualisations publiables (ex : LinkedIn)

---

## ⚙️ Stack Technique

| Étape         | Outil utilisé                     |
|---------------|-----------------------------------|
| Extraction    | Python + API Strava (requests)    |
| Stockage      | PostgreSQL                        |
| Transformation| DBT (staging + marts)             |
| Orchestration | Airflow (prévu pour v2)           |
| Analyse       | Jupyter, Pandas, Seaborn, Statsmodels |

---

## ✨ Compétences Développées

- Mise en place d’un pipeline ELT avec outils modernes
- Modélisation de données avec DBT (staging, marts)
- Connexion à une API REST & authentification OAuth
- Requêtes SQL complexes & automatisation PostgreSQL
- Analyses statistiques : corrélation, tendance, saisonnalité
- Visualisation de données chronologiques (matplotlib/seaborn)

---

## 📊 Exemples d’Insights Produits

- 📉 Baisse de la fréquence cardiaque moyenne à vitesse constante → gain d’endurance
- 🔁 Corrélation entre volume d’entraînement et amélioration physiologique
- 📆 Saisonnalité dans les performances (pics en été, creux en hiver)
- 📈 Progression annuelle des kilomètres, sorties, vitesse

---

## 🚀 Et après ?

- Ajout de **modèles de prédiction** (ex : temps futur sur course)
- Intégration d’un **dashboard interactif** (Streamlit ou Power BI)
- Automatisation complète avec **Airflow + Docker**
- Comparaison avec d’autres athlètes (social Strava API)

---

> Ce projet me permet de **mettre en pratique des compétences clés en ingénierie et analyse de données**, tout en valorisant des données personnelles concrètes et engageantes.
