Partie acquisition : 

La partie acquisition se décline en deux grandes étapes : 
-	La calibration des couleurs, qui permet de rendre notre détection invariante à la luminosité de l’environnement. Pour cela, l’utilisateur doit suivre les consignes qui consistent à afficher à l’écran la face dont le carré central est la couleur indiquée en haut de l’écran.
-	L’acquisition des faces : l’utilisateur présente une première face (aléatoire) du cube. Il doit suivre les consignes qui lui sont indiquées à l’écran (flèches) pour les faces suivantes. Durant ce processus, l’utilisateur devra remontrer la face frontale deux fois pour être sûr que l’orientation n’a pas changé.
Une fois l’acquisition finie, s’il n’y a pas d’erreurs liée à l’orientation. Un message de réussite est affiché à l’écran. L’utilisateur peut appuyer sur la touche “q” pour passer à la prochaine étape. Dans le cas contraire (acquisition erronée), un message d’erreur s’affiche et l’utilisateur doit recommencer l’acquisition des faces (sans passer par la calibration)

Technologies utilisées pour la détection : 
-	Utilisation de filtres: flou gaussien ,canny(),dilate() pour détecter l’ensemble des contours
-	Applications de conditions pour ne garder que les 9 contours correspondant aux facettes de la face:  propriétés d’un carré ( angle droit, cotés égaux) 
-	Distance entre l’objet et la caméra fixé à partir de la taille des surfaces des facettes
-	Détection des couleurs : on récupère la moyenne de la couleur de chaque facettes lorsqu’elle est acquise ( en RGB) et nous appliquons la distance CIE2000 avec les couleurs de références obtenues lors de la calibration.
