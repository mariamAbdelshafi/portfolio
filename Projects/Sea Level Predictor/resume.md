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

---

# 🌊 Sea Level Rise Visualization (Certification Data Analysis with Python, FreeCodeCamp)

## 📋 Description
This project analyzes historical sea level data and visualizes the rise in sea level over time.  
It uses Python, Pandas, Matplotlib, and SciPy to create scatter plots and linear regression trend lines.

Two trend lines are plotted:
1. A line based on all available years in the dataset.  
2. A line based on data from the year 2000 onward, showing recent trends.

## ⚙️ Main Features

1. **Data Loading**
   - Reads data from `epa-sea-level.csv`.  

2. **Scatter Plot**
   - Plots individual yearly measurements as points.  

3. **Trend Lines**
   - Computes and plots the line of best fit for all years (red).  
   - Computes and plots the line of best fit from 2000 onward (green).  

4. **Visualization**
   - Adds labels for the x-axis (`Year`) and y-axis (`Sea Level (inches)`).  
   - Adds a title (`Rise in Sea Level`) and a legend.  
   - Saves the plot as `sea_level_plot.png`.  

## 🧰 Tools & Technologies
- **Python**  
- **Pandas** — data manipulation  
- **Matplotlib** — plotting  
- **SciPy** — linear regression  
- **Environment**: VS Code

## 📈 Generated Output
- `sea_level_plot.png` → Scatter plot with two trend lines predicting future sea level rise  
