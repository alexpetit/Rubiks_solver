**Étapes pour faire fonctionner le Rubik’s Solver :**

- Télécharger le dossier de code et l’ouvrir dans un IDE python
- Créer un virtual environnement et l’activer ( . venv/bin/activate)
- Installer les librairies nécessaires (requirements) : pip install -r requirements.txt
- Exécuter le fichier main.py qui se trouve dans le dossier principal 

**La partie acquisition se lance :**

- Réaliser la calibration de la caméra : montrer les faces du rubik’s cube une à une comme indiqué en haut à gauche de l’écran. 
- Réaliser l’acquisition des faces : les faces sont demandées une à une en haut à gauche selon leur position (front, up, down, right, left, back), et un résumé des faces acquises s’affiche en bas à droite. S’il n’y a pas d’erreur l’acquisition est validée et il suffit d’appuyer sur ‘q’ pour quitter. 

**La partie Tutoriel se lance:** 

Le rubik’s cube s’affiche avec la configuration fournie lors de l’acquisition. L’affichage peut être modifié (rotation du cube) à l’aide des flèches du clavier. 
Afin de résoudre le rubik’s cube, il faut appuyer sur la touche entrée et une étape va être jouée à l’écran. En appuyant consécutivement sur cette touche, on arrive à la résolution du cube. 
Une fois terminé, il suffit de quitter la fenêtre. 
