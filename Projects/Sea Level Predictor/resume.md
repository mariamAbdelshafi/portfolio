# 🌊 Visualisation de la montée du niveau de la mer (Certification Data Analysis with python, FreeCodeCamp)

## 📋 Description
Ce projet analyse les données historiques du niveau de la mer et visualise l’augmentation du niveau de l’eau au fil du temps.  
Il utilise Python, Pandas, Matplotlib et SciPy pour créer des graphiques de dispersion et des lignes de tendance par régression linéaire.

Deux lignes de tendance sont tracées :
1. Une ligne basée sur toutes les années disponibles dans le dataset.  
2. Une ligne basée sur les données à partir de l’an 2000, illustrant les tendances récentes.

## ⚙️ Fonctionnalités principales

1. **Chargement des données**
   - Lecture des données depuis `epa-sea-level.csv`.  

2. **Graphique de dispersion**
   - Affiche les mesures annuelles comme des points individuels.  

3. **Lignes de tendance**
   - Calcule et trace la ligne de tendance pour toutes les années (rouge).  
   - Calcule et trace la ligne de tendance à partir de 2000 (vert).  

4. **Visualisation**
   - Ajoute les labels pour l’axe X (`Year`) et l’axe Y (`Sea Level (inches)`).  
   - Ajoute un titre (`Rise in Sea Level`) et une légende.  
   - Enregistre le graphique sous `sea_level_plot.png`.  

## 🧰 Outils et technologies
- **Python**  
- **Pandas** — manipulation des données  
- **Matplotlib** — visualisation graphique  
- **SciPy** — régression linéaire 
- **Environnement**: Vs Code

## 📈 Résultat produit
- `sea_level_plot.png` → Graphique de dispersion avec deux lignes de tendance prédisant l’élévation future du niveau de la mer  
