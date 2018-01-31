from rest_framework import permissions
from oauth2_provider.models import AccessToken

# ----------------------------------------------------------------------------------------------------
class IsauthenticatedD(permissions.BasePermission):
	message='vous n  avez pas le droit d effectuer cette action'
	def has_permission(self, request, view):
		#print(request.META['HTTP_ORIGIN'])
		if 'HTTP_AUTHORIZATION' in request.META.keys():
			try:
				queryset_token = AccessToken.objects.filter(token=request.META['HTTP_AUTHORIZATION']).first()
				print((request.META['HTTP_ORIGIN'] in queryset_token.application.redirect_uris))
				if not (queryset_token.is_expired()):
					return queryset_token.user.is_active 
				else:
					return False
			except Exception:
				return False
		else:
			return request.user.is_active and request.user.is_authenticated
# --------------------------------------------------------------------------------------------------
class HeaderContainToken(permissions.BasePermission):
	"""docstring for HeaderContainToken"""
	message={'error': 'vous n  avez pas le droit d effectuer cette action'}
	def has_permission(self, request, view):
		if 'HTTP_AUTHORIZATION' in request.META.keys():
			if request.META['HTTP_AUTHORIZATION']:
				return True
			else:
				return False

# ---------------------------------------------------------------------------------------------------
class IsAdmin(permissions.BasePermission):
	"""docstring for EstAmi"""
	def has_permission(self, request, view):
		if 'HTTP_AUTHORIZATION' in request.META.keys():
			try:
				queryset_token = AccessToken.objects.filter(token=request.META['HTTP_AUTHORIZATION']).first()
				if not (queryset_token.is_expired()):
					return queryset_token.user.is_superuser
				else:
					return False
			except Exception:
				return False
		else:
			return request.user.is_superuser and request.user.is_authenticated
# -----------------------------------------------------------------------------------------------------





#class BasePermission(object):


    #def has_permission(self, request, view):

        #return True

    #def has_object_permission(self, request, view, obj):

        #return True


		
		#print(dir(request))
		# print(request.data)
		# print('---------------------------------')
		# print(request.query_params)
		# print('---------------------------------')
		# print(request.method)
		# print('---------------------------------')
		# print(request.successful_authenticator)
		# print('---------------------------------')
		# print(request.accepted_media_type)
		# print(request.accepted_media_type)
		# print('---------------------------------')
		# print(request.accepted_renderer)
		# print('-------------Authentication--------------------')
		# print(request.auth)
		# print('---------------------------------')
		# print(request.content_type)
		# print('---------------------------------')
		# print(request.force_plaintext_errors)
		# print(request.negotiator)
		# print('---------------------------------')
		# print(request.parser_context)
		# print('---------------------------------')
		# print(request.parsers)
		# print('---------------------------------')
		# print(request.stream)
		# print('---------------------------------')
		# print(request.version)
		# print('---------------------------------')
		# print(request.user)
		# print('---------------------------------')
		# print(request.versioning_scheme)
		# print(request.META['HTTP_AUTHORIZATION'])
		# print(dir(request))
		# print('---------------Fin------------------')