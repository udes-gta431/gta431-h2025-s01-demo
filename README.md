# GTA-431 H2025 - Cours 1

Ce script Python permet d'explorer le metadata associé à un Dataframe pandas.
Les données utilisées proviennent du recensement des crimes de la ville de Montréal.
Vous pouvez consulter la source sur ce lien: https://donnees.montreal.ca/dataset/actes-criminels#data


## Analyse du metadata d'un jeu de données avec Pandas
| Méthode                      | Description                                                                                       |
|------------------------------|---------------------------------------------------------------------------------------------------|
| `pd.read_csv("chemin/vers/le/fichier.csv")` | Retourne un objet DataFrame à partir du fichier CSV fourni en entrée.                        |
| `df.describe()`              | Retourne des statistiques descriptives (moyenne, écart-type, min, max, etc.) pour les colonnes numériques. |
| `df.head()`                  | Retourne les 5 premières lignes du DataFrame pour un aperçu rapide des données.                  |
| `df.columns`                 | Retourne les noms de toutes les colonnes du DataFrame.                                           |
| `df.info()`                  | Retourne des informations générales sur le DataFrame, telles que le nombre de lignes, colonnes, types de données et mémoire utilisée. |
| `df.dtypes`                  | Retourne les types de données de chaque colonne (e.g., int, float, object).                     |
| `df.shape`                   | Retourne les dimensions du DataFrame (nombre de lignes, nombre de colonnes).                    |
