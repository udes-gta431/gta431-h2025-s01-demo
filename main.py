"""
Michaël Sauget (2025-01-07)

Ce script Python permet d'explorer le metadata associé à un Dataframe pandas.
Les données utilisées proviennent du recensement des crimes de la ville de Montréal.
Vous pouvez consulter la source sur ce lien: https://donnees.montreal.ca/dataset/actes-criminels#data

"""

# Importation de la bibliothèque Pandas pour manipuler les données tabulaires
import pandas as pd


# Lire le fichier CSV (Comma Separated Values) contenant les actes criminels à Montréal et créer un DataFrame
df = pd.read_csv("actes-criminels.csv")


# Afficher des statistiques descriptives (moyenne, écart-type, min, max, etc.) pour les colonnes numériques
# print(df.describe())


# Afficher les 5 premières lignes du DataFrame pour un aperçu rapide des données
# print(df.head())


# Afficher les noms de toutes les colonnes du DataFrame
# print(df.columns)


# Afficher des informations générales sur le DataFrame, telles que le nombre de lignes, colonnes, types de données et mémoire utilisée
# print(df.info())


# Afficher les types de données de chaque colonne (e.g., int, float, object)
# print(df.dtypes)


# Afficher les dimensions du DataFrame (nombre de lignes, nombre de colonnes)
# print(df.shape)
