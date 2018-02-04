"""
La ligne ci-dessous représente une url contenant des paramètres.
Comme dit dans la description de l'attaque par pollution de paramètres HTTP
les noms des paramètres doivent être differents.
"""
url('^utilisateurs/(?P<pseudo>.+)/(?P<nom>.+)$', UtilisateursList.as_view()),

"""
Pour recuperer ces paramètres nous allons utiliser une fonction qui pour être personnalisée 
"""
def function (request, *args, **kwargs):
	PSEUDO=kwargs["pseudo"]
	NOM=kwargs["nom"]
   """
   Et en suite effectuer les contrôles sur les paramètres.
   Avec le DRF c'est l'objet  kwargs  ou args qui est utilisé pour recuperer les valeurs des
   paramètres.
   """