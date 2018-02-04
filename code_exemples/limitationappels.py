"""
Pour les limitations d'appel de l'API, le DRF met à la disposition des programmeurs la bibliothèque disponible sous le 
chemin suivant: from rest_framework import throttling. 
La bibliothèque throttling de DRF se base sur les caches pour gérer les taux d'appel
"""
#Pour utiliser la bibliothèque il faut ajouter les instructions suivantes dans le fichier settings du projet.
CACHES={
    'default':{
    'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
    'LOCATION': 'cache_db'
    }
}
# puis créer la table des cache en executant la commande suivante:
python manage.py createcachetable

"""
Pour personnaliser le message de retour on procède de la manière suivantes
"""

from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled

def nom_de_la_fonction_personnalisee(exc, context):
	response = exception_handler(exc, context)
	if isinstance(exc, Throttled): 
		custom_response_data = { 'error': ' Vous avez fait trop de requêtes'}
		response.data = custom_response_data
	return response
"""
Cette fonction doit être définie  dans un fichier qui sera appelé dans le fichier settings comme suit:
"""
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'chemin_fichier_de_la_fonction_de_limitation.nom_de_la_fonction_personnalisee',
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/min',
        'user': '10/min'
    }
}

"""
Avec cet exemple, nous utilisons les scopes de base (anon et user), 
anon pour anonyme, user pour les utilisateur connecté.
ici l'utilisateur anonyme ne peut faire que 2 requêtes par minutes. Et l'utilisateur connecté 10. 
Les scopes sont en suite utilisés dans les views de la manière suivante.
"""
throttle_scope = 'user'
throttle_scope = 'anon'

"""
Pour plus de détails prière de consulter le lien suivant:
"""
http://www.django-rest-framework.org/api-guide/throttling/