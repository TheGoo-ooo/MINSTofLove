# MINSTofLove

Application de classification permettant de reconna�tre des chiffres de 0 � 9 dans des images de 28x28 pixels. Une image contient un ou aucun chiffre, l'algorithme doit �tre capable de d�tecter un non-chiffre "NaN". Les algorithmes de classifications sont entra�n�s ou d�velopp�s avec la base de donn�es MINST.
>http://yann.lecun.com/exdb/mnist/

## Interface

*Responsable:  Gabriel Griesser*

![Example of interface that would correspond to our needs](https://raw.githubusercontent.com/TheGoo-ooo/MINSTofLove/master/ressources/recognizing-two.png)
Image non repr�sentative du r�sultat final

- Affichage de la classification
- Canevas de dessin noir et blanc
- Import et traitement d'image
- Choix de l'algorithme de classification

## Algorithme de classification

*Responsables: Florian Fasmeyer et Julien Feuillade*

- Trouver et lire des donn�es
- DNN feed forward avec back propagation
- Classifieur du plus proche voisin

## Traitement des images

*Responsable Luca Srdjenovic*

- Mise en noir et blanc
- Suppression de bruit
- fermeture puis ouverture