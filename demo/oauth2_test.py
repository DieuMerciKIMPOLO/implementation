#https://github.com/RichardKnop/django-oauth2-server
#01 password
#https://github.com/evonove/django-oauth-toolkit/blob/master/docs/rest-framework/getting_started.rst
client_id='pzpZDp6pqXZJiXMvqQpcBSnoNTXvisnAg9pC3Ws0'
client_secret='QzuWkLkH4Kef8rXtpwnNLvniLPFsC22LtJ5RXMJRBExcImT5mDGu2vfNylYBHR9lLeWPzbufg6SnYuwuTdKxlvplOosO0oULGuMtaAIIKn3oWvGx65fD5N2vBHR0SSLW'
#CURL requests
	#Type of grant password
	#curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/
    curl -X POST -d "grant_type=password&username=dieumerci&password=dieumerci" -u"pzpZDp6pqXZJiXMvqQpcBSnoNTXvisnAg9pC3Ws0:QzuWkLkH4Kef8rXtpwnNLvniLPFsC22LtJ5RXMJRBExcImT5mDGu2vfNylYBHR9lLeWPzbufg6SnYuwuTdKxlvplOosO0oULGuMtaAIIKn3oWvGx65fD5N2vBHR0SSLW" http://localhost:8000/o/token/
    
    #La reponse
    {
    	"access_token": "ekAVL6OCkbPLNpv2eGFMEv0gmuoQ1w", 
    	"expires_in": 36000, 
    	"refresh_token": "mtSMLFHChqiFQVc90Fb8OoJi245mRq", 
    	"token_type": "Bearer",
    	"scope": "read write"
   }

# Retrieve users
curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/users/
curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/users/1/

# Retrieve groups
curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/groups/

# Insert a new user
curl -H "Authorization: Bearer <your_access_token>" -X POST -d"username=foo&password=bar" http://localhost:8000/users/


curl -X POST -d "grant_type=password&username=<user_name>&password=<password>&scope=read" -u"5wDpK1bbsqZOOmX8Kn4h6Vdd6INXGu3dbHTC1w27:<client_secret>" http://localhost:8000/o/token/
#https://curl.trillworks.com/
data = [
  ('grant_type', 'password'),
  ('username', '<user_name>'),
  ('password', '<password>'),
  ('scope', 'read'),
]
response = requests.post('http://localhost:8000/o/token/', data=data, auth=('<client_id>', '<client_secret>'))

#02 Authorization code 
client_id='5A3UHsRYALnDNsrrX2R4gqkhGsmM9UzlUDNCXhq2'
client_secret='mmFlteIyDjCYs8rGSLhERWojZh5buXBFV2prulTtuTz52n6d0J0Gvc7C0WYOo3WPyttYVdxgn04i1gmwz8itbFouU3VNbQitm2wNMg2b7tUkx5qDqe2AAwrND1ylTzRR'



#03 implicit
client_id='5wDpK1bbsqZOOmX8Kn4h6Vdd6INXGu3dbHTC1w27'
client_secret='N52qOwShEWZB13GAzr8yphQmmPfE7gjoIQsuZEim6aCMflKMJjbxHeapAiQkTwR8xbDpPAnbhwpaoeRi5tTKpHO1fqKCIzSSalLPYElTGPXoQX3HVJ2Z96PzHuBPa0x9'
http://localhost:8000/o/authorize/?response_type=token&client_id=5wDpK1bbsqZOOmX8Kn4h6Vdd6INXGu3dbHTC1w27&redirect_uri=http://localhost:3000/&state=
http://127.0.0.1:8000/#expires_in=36000&state=&scope=write+read&access_token=NfiEKzEMREae4wVS3hbcE9BrGlu3XU&token_type=Bearer
curl -H "Authorization: Bearer lLyxlYeoBPjQA3mAKtyHBvtf4Qymhd" http://127.0.0.1:8000/demof/utilisateurs/liste/
curl -H "Authorization: a1sowQsl3C0pAPgS7m12y5t6AK2RXg" http://127.0.0.1:8000/demof/utilisateurs/liste/
curl -H "Authorization:  9Y068TJAQXurdqk37GdO5uW0I5wchv" http://127.0.0.1:8000/demof/utilisateurs/profil/
#http://localhost:8000/web/authorize/?response_type=code&client_id=testclient&redirect_uri=https://www.example.com&state=somestate

#04 client credential
client_id='5wDpK1bbsqZOOmX8Kn4h6Vdd6INXGu3dbHTC1w27'
client_secret='EMYokv0gVGtfpLn954wlSlctMKY7S6QGBoJG5Ypd37PGR15MrqTJacD2UcsHDOXEBUgA2twWQb9QcMEISVafp88zthVsPFv73CkihnPWLoJOQQ17NUyOkB1VwlFmyuYp'

curl -X POST -d "grant_type=client_credentials" -u"iINIbrzOLv7DJNztk3evZlUCSirvC4zYl6deKMrI:EMYokv0gVGtfpLn954wlSlctMKY7S6QGBoJG5Ypd37PGR15MrqTJacD2UcsHDOXEBUgA2twWQb9QcMEISVafp88zthVsPFv73CkihnPWLoJOQQ17NUyOkB1VwlFmyuYp" http://localhost:8000/o/token/

Refresh Token

Let's say you have created a new access token using the user credentials grant type. The response included a refresh token which you can use to get a new access token before your current access token expires.

$ curl -u testclient:testpassword localhost:8080/api/v1/tokens/ -d 'grant_type=refresh_token&refresh_token=55697efd4b74c980f2c638602556115bc14ca931'
