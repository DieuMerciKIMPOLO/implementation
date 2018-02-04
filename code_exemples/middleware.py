
class nom_du_middleware(object):
    """
    object peut être une autre classe de type middleware
    """
    def process_request(self, request):
        """
        les instructions
        """
        pass

    def process_response(self, request, response):
        """
        les instructions
        """
        return response

    """
    Ce sont les deux fonctions qui permettent d'intercepter les 
    requêtes et leur réponse.
    Pour utiliser un middleware, il faut l'inseré dans le fichier settings de 
    la manière suivante:
    """
MIDDLEWARE = [
    'chemin_vers_le_fichier_du_middleware.nom_du_middleware',
]