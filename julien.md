# Animator 
Nous avons utilisé pour cette partie la librairie OpenGL qui permet d’afficher et de faire des calculs sur les images 2D et 3D. Dans notre projet, les fonctions d’openGL nous ont permis de dessiner les 27 cubes qui composent le rubik’s-cube. 

Nous utilisons aussi le package « pygame » qui est très utilisé pour la conception de jeu vidéo en python. Sur ce projet, il permet de rendre le tutoriel interactif en appuyant sur la touche « ENTER » pour passer à l’étape suivante.  

Enfin nous avons comme pour la partie acquisition utilisée le package « kociemba » qui renvoie les étapes de mouvement pour résoudre un Rubik’s-cube. Nous avons ensuite traité ces données afin de matcher ces informations avec la représentation graphique.


Lors de la récupération des informations de l’acquisition, nous initialisons un rubik’s-cube résolu (toutes les faces ont une couleur unique). 
Dans un second temps, grâce à la fonction « solve » de kociemba, nous programmons les rotations inverse qui permet de mélanger le Rubik’s-cube. Cette étape est codée dans l’initialisation du cube entier, nous ne l’apercevons pas sur l’écran.
Enfin, nous affichons les rotations à faire pour résoudre le cube chaque fois que l’on appuie sur la touche « ENTER ».
