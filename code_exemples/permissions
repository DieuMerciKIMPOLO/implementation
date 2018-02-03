'''
 Cette permission permet de verifier que:
 -l'en-tête de la requête de l'utilisateur contient bien l'en-tête HTTP_AUTHORIZATION, 
 -le token de l'utilisateur est valide 
 -la source de la requête est  fiable.
'''
from rest_framework import permissions
from oauth2_provider.models import AccessToken

class IsauthenticatedD(permissions.BasePermission):
	message='vous n  avez pas le droit d effectuer cette action'
	def has_permission(self, request, view):
		if 'HTTP_AUTHORIZATION' in request.META.keys():
			try:
				queryset_token = AccessToken.objects.filter(token=request.META['HTTP_AUTHORIZATION']).first()
				if not (queryset_token.is_expired()) and (request.META['HTTP_ORIGIN'] in queryset_token.application.redirect_uris):
					return queryset_token.user.is_active 
				else:
					return False
			except Exception:
				return False
		else:
			return False
'''
Pour utiliser une permissions du DRF dans les views, on ajoute l'instruction dans la view concernée:
permission_classes = (nom_de_la_permission,)
'''