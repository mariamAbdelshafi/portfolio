# ✋ Contrôle du volume par gestes de la main

## 📋 Description
Ce projet permet de contrôler le volume du système à l’aide de gestes de la main, capturés en temps réel par la webcam.  
Grâce à MediaPipe, le programme détecte la main et suit les positions des doigts afin de mesurer la distance entre le pouce et l’index.  
Cette distance est ensuite utilisée pour ajuster dynamiquement le volume du système à l’aide de PyCaw.  

Plus les doigts sont éloignés, plus le volume augmente — et inversement.

## ⚙️ Fonctionnalités principales

1. **Détection de la main en temps réel**
   - Utilisation de MediaPipe Hands pour détecter et suivre les points clés de la main via la webcam.  

2. **Mesure de distance**
   - Calcul de la distance euclidienne entre le bout du pouce et celui de l’index.  

3. **Contrôle du volume**
   - Conversion de la distance mesurée en un niveau de volume via une interpolation linéaire.  

4. **Retour visuel**
   - Affichage à l’écran de la distance calculée et du volume en pourcentage.  

5. **Interaction utilisateur**
   - Appuyer sur **Q** pour quitter l’application.  

## 🧰 Outils et technologies
- **Python**  
- **OpenCV** — capture et traitement vidéo en temps réel  
- **MediaPipe** — détection et suivi de la main  
- **PyCaw** — contrôle du volume système (Windows)  
- **NumPy** — calculs numériques  
- **Math** — calcul de distance  

## 📈 Résultat
- Flux vidéo en direct affichant la main détectée et les repères des doigts.  
- Le volume s’ajuste automatiquement selon la distance entre le pouce et l’index.  
- Appuyer sur Q pour fermer la fenêtre.  

---

# ✋ Hand Gesture Volume Control 

## 📋 Description
This project allows you to control the system volume using hand gestures, captured in real time through your webcam.  
With MediaPipe, the program detects and tracks hand landmarks to measure the distance between the thumb and index finger.  
This distance is then used to dynamically adjust the system’s volume via PyCaw.  

The farther apart your fingers are, the higher the volume — and vice versa.

## ⚙️ Key Features

1. **Real-time hand detection**
   - Uses MediaPipe Hands to detect and track hand landmarks from the webcam feed.  

2. **Distance measurement**
   - Calculates the Euclidean distance between the thumb tip and the index fingertip.  

3. **Volume control**
   - Converts the measured distance into a system volume level using linear interpolation.  

4. **Visual feedback**
   - Displays the measured distance and current volume percentage on the video feed.  

5. **User interaction**
   - Press Q to quit the application.  

## 🧰 Tools and Technologies
- **Python**  
- **OpenCV** — real-time video capture and processing  
- **MediaPipe** — hand detection and landmark tracking  
- **PyCaw** — system volume control (Windows)  
- **NumPy** — numerical computations  
- **Math** — distance calculation  

## 📈 Output
- Real-time video feed showing hand detection and tracked landmarks.  
- Volume automatically adjusts based on the distance between the thumb and index finger.  
- Press Q to close the window.  
