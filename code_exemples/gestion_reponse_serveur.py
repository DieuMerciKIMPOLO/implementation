"""
Le DFR met à la disposition des développeurs labibliothèque sous le chemin suivant:
from rest_framework import status contenant tout les code de message HTTP. De plus avec le DRF les response sont gérées 
avec l'objet Response disponible sous le chemin from rest_framework.response import Response.
Le conseil ici c'est d'utiliser les réponse générique accompagnées de code appropriés

"""
from rest_framework.response import Response
from rest_framework import status
from demo.models import Profilutilisateur

class ProfilutilisateurViewAdd(generics.CreateAPIView):
    """
        Creation d'un utilisateur avec un modele personnalisee
    """
    queryset = Profilutilisateur.objects.all()
    serializer_class = ProfilutilisateurSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data_errors = {}
            data_message = str('')
            for P, M in serializer.errors.items():
                data_message += P + ": " + M[0].replace(".", '')
            data_errors['error'] = data_message
            return Response({
                        'error':'Tous les champs sont obligatoires'
                    }, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'message':'Utilisateur cree avec succes'}, status=status.HTTP_201_CREATED)

"""
Avec cette exemple en cas d'échec les détail de l'echec sont dans la variable data_errors. Mais pour être générique 
puis utiliser un code approprié la réponse doit être definie de la manière suivante:
return Response({'error':'Tous les champs sont obligatoires'}, status=status.HTTP_400_BAD_REQUEST).
Pour le cas de succès aussi le message est générique et accompagné d'un code approprié:
return Response({'message':'Utilisateur cree avec succes'}, status=status.HTTP_201_CREATED)
"""