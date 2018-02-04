#from rest_framework import throttling
from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled

def custom_exception_handler(exc, context):
	response = exception_handler(exc, context)
	if isinstance(exc, Throttled): 
		custom_response_data = { 'error': ' Vous avez fait trop de requêtes'}
		response.data = custom_response_data
	return response