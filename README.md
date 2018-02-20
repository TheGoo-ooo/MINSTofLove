# MINSTofLove

Application de classification permettant de reconnaître des chiffres de 0 à 9 dans des images de 28x28 pixels. Une image contient un ou aucun chiffre, l'algorithme doit être capable de détecter un non-chiffre "NaN". Les algorithmes de classifications sont entraînés ou développés avec la base de données MINST.
>http://yann.lecun.com/exdb/mnist/

## Interface

*Responsable:  Gabriel Griesser*

![Example of interface that would correspond to our needs](https://raw.githubusercontent.com/TheGoo-ooo/MINSTofLove/master/ressources/recognizing-two.png)
Image non représentative du résultat final

- Affichage de la classification
- Canevas de dessin noir et blanc
- Import et traitement d'image
- Choix de l'algorithme de classification

## Algorithme de classification

*Responsables: Florian Fasmeyer et Julien Feuillade*

- Trouver et lire des données
- DNN feed forward avec back propagation
- Classifieur du plus proche voisin

## Traitement des images

*Responsable Luca Srdjenovic*

- Mise en noir et blanc
- Suppression de bruit
- fermeture puis ouverture