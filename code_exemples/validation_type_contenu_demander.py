'''
Avec le DRF, les types de contenus demandés sont contenus dans l'object request.
Soit HTTP_ACCEPT_DEFINE la variable qui contient les types de contus acceptables. 
'''
def ValidationTypeContenuDemande(request):
	if request.META['HTTP_ACCEPT'] in HTTP_ACCEPT_DEFINE:
		return True
