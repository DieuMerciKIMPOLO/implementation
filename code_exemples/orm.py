"""
Nous allons mettre en evidence l'utilisation de l'ORM, nous allons nous basés sur le modèle 
Profilutilisateur qui représente la table Profilutilisateur. Nous allons selectionner les informations d'un utilisateur 
qui possède l'identifiant dans la variable UTILISATEUR_ID dans cette table Profilutilisateur.
"""
from django.db.models import Q
from demo.models import Profilutilisateur

REPONSE=Profilutilisateur.objects.filter(Q(id=UTILISATEUR_ID)).first()
#La variable REPONSE est objet, pour acceder au nom on procède de la manière suivante
NOM=REPONSE.nom

"""
L'ORM de DRF, permet d'éviter les injections SQL.
"""

