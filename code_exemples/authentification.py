
def CheckPassword(request,ch_password):
    '''
      Cette fonction par exemple permet de définir le pourcentage de complexité d'un 
      mot de passe. la somme des coefficients fait 15
      Une lettre en majuscule =1
      Une valeur numerique=2
      Un caractère spécial=3
      La longuer d'au-moins 8 caractères=8
      Une lettre en miniscule=1
      Lors de la création d'un compte cette fonction peut être utilisée pour rejeter les mots
      de passe d'un pourcentage donné.
    '''
    invalidChars = set(string.punctuation.replace("_", ""))
    controle_password=ch_password
    ISUPPER=0
    ISDIGIT=0
    ISLOWER=0
    INVALIDCHARS=0
    LENGTH=0

    if any(x.isupper() for x in controle_password):
        ISUPPER=1
    if any(x.isdigit() for x in controle_password) :
        ISDIGIT=2
    if any(x in invalidChars for x in controle_password):
        INVALIDCHARS=3
    if len(controle_password)>7:
        LENGTH=8
    if any(x.islower() for x in controle_password):
        ISLOWER=1
    if int(ISUPPER+ISLOWER)==2 and int(INVALIDCHARS+ISDIGIT)==0:
        return HttpResponse(json.dumps({'percentage':float((3+LENGTH)/15)*100}))
    else:
        return HttpResponse(json.dumps({'percentage':float((INVALIDCHARS+ISLOWER+ISDIGIT+ISUPPER+LENGTH)/15)*100}))



"""
Aussi le DRF fournit un système de stockage de mots de passe souple et emploie PBKDF2 par défaut. 
Avec une fonction de hachage SHA256, un mécanisme d’étirement de mot de passe recommandé par le NIST
Cela devrait suffire pour la plupart des utilisateurs : c’est un algorithme bien sécurisé et exigeant 
d’énormes quantités de puissance de calcul pour être cassé. Il est également possible d'utiliser 
les password validators comme 

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
 voir----> https://docs.djangoproject.com/fr/2.0/topics/auth/passwords/
"""