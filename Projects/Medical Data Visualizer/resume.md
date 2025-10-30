# 🧠 Visualisation de données médicales (Certification Data Analysis with Python, FreeCodeCamp)

### 📋 Description
Ce projet vise à analyser un ensemble de données médicales et à visualiser les relations entre plusieurs indicateurs de santé 
(tels que le cholestérol, la glycémie, le poids et l’activité physique) et la présence de maladies cardiovasculaires.  
L’analyse repose sur Pandas pour le nettoyage et la manipulation des données, et sur Seaborn/Matplotlib pour la visualisation graphique.

### ⚙️ Fonctionnalités principales

1. **Normalisation des données**
   - Calcul de l’indice de masse corporelle (IMC) pour identifier les individus en surpoids.  
   - Normalisation des variables `cholesterol` et `gluc` en valeurs binaires (sain / à risque).  
   - Filtrage des valeurs aberrantes dans la tension, la taille et le poids.  

2. **Visualisation catégorielle (`draw_cat_plot`)**
   - Affiche la répartition de six variables (`active`, `alco`, `cholesterol`, `gluc`, `overweight`, `smoke`)  
     selon la présence ou non de maladies cardiovasculaires (`cardio`).  
   - Génère un diagramme en barres pour comparer les proportions de chaque catégorie.

3. **Carte de corrélation (`draw_heat_map`)**
   - Calcule la matrice de corrélation entre les variables médicales.  
   - Affiche une heatmap pour mettre en évidence les corrélations significatives.  
   - Masque la moitié supérieure du graphique pour une meilleure lisibilité.

### 🧰 Outils et technologies
- **Python**
- **Pandas** — nettoyage et transformation des données  
- **NumPy** — calculs numériques  
- **Seaborn** & **Matplotlib** — visualisation graphique  
- **Environnement**: VS Code

### 📈 Résultats produits
- `catplot.png` → Visualisation catégorielle des indicateurs de santé  
- `heatmap.png` → Carte de corrélation des variables médicales  

---

# 🧠 Demographic Data Analyzer (Data Analysis with Python Certification, FreeCodeCamp)

### 📋 Description
This project analyzes a medical dataset and visualizes the relationships between several health indicators 
(such as cholesterol, glucose, weight, and physical activity) and the presence of cardiovascular disease.  
The analysis uses Pandas for data cleaning and manipulation, and Seaborn/Matplotlib for graphical visualization.

### ⚙️ Main Features

1. **Data Cleaning & Normalization**
   - Computes Body Mass Index (BMI) to identify overweight individuals.  
   - Normalizes `cholesterol` and `gluc` into binary indicators (healthy / at risk).  
   - Filters out outliers in blood pressure, height, and weight.  

2. **Categorical Plot (`draw_cat_plot`)**
   - Displays the distribution of six variables (`active`, `alco`, `cholesterol`, `gluc`, `overweight`, `smoke`)  
     based on the presence or absence of cardiovascular disease (`cardio`).  
   - Generates a **bar chart** to compare proportions between categories.

3. **Heat Map (`draw_heat_map`)**
   - Calculates the correlation matrix between medical variables.  
   - Produces a **heatmap** to highlight significant correlations.  
   - Masks the upper triangle of the plot for better readability.

### 🧰 Tools & Technologies
- **Python**
- **Pandas** — data cleaning and transformation  
- **NumPy** — numerical computations  
- **Seaborn** & **Matplotlib** — data visualization  
- **Environment**: VS Code

### 📈 Generated Outputs
- `catplot.png` → Categorical visualization of health indicators  
- `heatmap.png` → Correlation heatmap of medical features  
