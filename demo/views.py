from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from oauth2_provider.models import AccessToken
from rest_framework import generics
from rest_framework import viewsets
from demo.serializer import *
from demo.permissions import *
from demo.throttling import *
from demo.models import *
from django.db.models import Q

def Recuperer_amis_id(data):
    LIST_AMIS=[]
    for connexion in data:
        LIST_AMIS.append(connexion['utilisateur_demandeur'])
        LIST_AMIS.append(connexion['utilisateur_confirmateur'])
    return LIST_AMIS
def HttpHeaders():
    HEADERS={
       'Cache-Control':'no-cache',
       'X-Content-Type-Options': 'nosniff',
       'X-Frame-Options': 'DENY',
       'Strict-Transport-Security': 'max-age=31536000; includeSubDomains'
    }
    return HEADERS
class ProfilutilisateurViewAdd(generics.CreateAPIView):
    """
        Creation d'un utilisateur avec un modele personnalisee
    """
    #permission_classes = (AllowAny,)
    #permission_classes = (IsAdmin,)
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

class ProfilView(generics.ListAPIView):
    """docstring for Profil"""
    #permission_classes = (IsAuthenticateD, )
    queryset_token= Profilutilisateur.objects.all()
    serializer_class=ProfilutilisateurListSerializer
    def list(self, request,*args, pk=None):
        try:
            queryset=AccessToken.objects.filter(token=request.META['HTTP_AUTHORIZATION']).first().user
            serializer = self.get_serializer(queryset)
            return Response(serializer.data)
        except Exception:
            return Response({"error":'Mauvaise demande'}, status=status.HTTP_400_BAD_REQUEST) 

# class ProfilutilisateurViewList(generics.ListAPIView):
#     """
#         Liste  des utilisateurs du modele Profilutilisateur
#     """
#     #permission_classes = (AllowAny,)
#     permission_classes = (IsAuthenticated, IsAdmin)
#     queryset = Profilutilisateur.objects.all()
#     serializer_class = ProfilutilisateurSerializer
#     #throttle_scope = 'anon'
class ProfilutilisateurViewList(generics.ListAPIView):
    """
        Liste  des utilisateurs du modele Profilutilisateur
    """
    #permission_classes = (CustomerAccessPermission,)
    #permission_classes = (HeaderContainToken,)
    queryset = Profilutilisateur.objects.all()
    serializer_class = ProfilutilisateurSerializer
    throttle_scope = 'user'
    def list(self, request, *args, pk=None):
        try:
            if 'HTTP_AUTHORIZATION' in request.META.keys():
                queryset_token = AccessToken.objects.filter(token=request.META['HTTP_AUTHORIZATION']).first()
                if queryset_token.user.is_superuser:
                    queryset = Profilutilisateur.objects.all()
                    serializer = self.get_serializer(queryset, many=True)
                    return Response(serializer.data)
                else:
                    list_amis=Connexion.objects.filter((Q(utilisateur_demandeur=queryset_token.user)|Q(utilisateur_confirmateur=queryset_token.user))&Q(statu_de_connexion=True)).values('utilisateur_demandeur','utilisateur_confirmateur')
                    print(list_amis)
                    queryset = Profilutilisateur.objects.filter(Q(id__in=Recuperer_amis_id(list_amis))|Q(id=queryset_token.user.id))
                    serializer = self.get_serializer(queryset, many=True)
                    return Response(serializer.data)

            else:
                if request.user.is_superuser:
                    queryset = Profilutilisateur.objects.all()
                    serializer = self.get_serializer(queryset , many=True)
                    return Response(serializer.data)
                else:
                    list_amis=Connexion.objects.filter((Q(utilisateur_demandeur=request.user)|Q(utilisateur_confirmateur=request.user))&Q(statu_de_connexion=True)).values('utilisateur_demandeur','utilisateur_confirmateur')
                    queryset = Profilutilisateur.objects.filter(Q(id__in=Recuperer_amis_id(list_amis))|Q(id=queryset_token.user.id))
                    serializer = self.get_serializer(queryset, many=True)
                    return Response(serializer.data)
        except Exception as e:
            return Response({"status": "failure", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#----------------------------------------------------------------------------------------------------------------------------------------
        

class RoleUtilisateurViewAdd(generics.CreateAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (AllowAny,)
    queryset = RoleUtilisateur.objects.all()
    serializer_class = RoleUtilisateurSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data_errors = {}
            data_message = str('')
            for P, M in serializer.errors.items():
                data_message += P + ": " + M[0].replace(".", '')
            data_errors['error'] = data_message
            return Response(data_errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RoleUtilisateurViewList(generics.ListAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (AllowAny,)
    queryset = RoleUtilisateur.objects.all()
    serializer_class = RoleUtilisateurSerializer
#--------------------------------------------------------------------------------------------------
class CommentairesViewList(generics.ListAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (AllowAny,)
    queryset = Commentaires.objects.all()
    serializer_class = CommentairesListSerializer
    def list(self, request, *args, pk=None):
        try:
            queryset_token = AccessToken.objects.filter(token=request.META['HTTP_AUTHORIZATION']).first()
            if queryset_token.user.is_superuser:
                LIST_COMMENTS=[]
                queryset = Commentaires.objects.all()
                serializer = self.get_serializer(queryset, many=True)
                for C in serializer.data:
                    LIST_COMMENTS.append({
                        'utilisateur':Profilutilisateur.objects.filter(id=C['utilisateur']).first().nom_utilisateur,
                        'commentaire':C['commentaire'],
                        'date_post':C['date_post']
                        }
                        )
                return Response(LIST_COMMENTS)
            else:
                LIST_COMMENTS=[]
                queryset = Commentaires.objects.filter(Q(utilisateur=queryset_token.user))
                serializer = self.get_serializer(queryset, many=True)
                for C in serializer.data:
                    print(C['utilisateur'])
                    LIST_COMMENTS.append({
                        'utilisateur':Profilutilisateur.objects.filter(id=C['utilisateur']).first().nom_utilisateur,
                        'commentaire':C['commentaire'],
                        'date_post':C['date_post']
                        }
                        )
                return Response(LIST_COMMENTS)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CommentairesViewAdd(generics.CreateAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (IsauthenticatedD,)
    queryset = Commentaires.objects.all()
    serializer_class = CommentairesAddSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data_errors = {}
            data_message = str('')
            for P, M in serializer.errors.items():
                data_message += P + ": " + M[0].replace(".", '')
            data_errors['error'] = data_message
            return Response({
                        'error':'Ce champs est obligatoire'
                    }, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                profilutili=AccessToken.objects.filter(token=request.META['HTTP_AUTHORIZATION']).first()
                serializer.save(utilisateur=profilutili.user)
                return Response({'message':'Commentaire posté avec succès'}, status=status.HTTP_201_CREATED)
            except Exception:
                return Response({'error':'Rassurez vous que vous etes connecté'}, status=status.HTTP_400_BAD_REQUEST)
        
#----------------------------------------------------------------------------------------------------------

class CitationViewAdd(generics.CreateAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (AllowAny,)
    queryset = Citations.objects.all()
    serializer_class = CitationsSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data_errors = {}
            data_message = str('')
            for P, M in serializer.errors.items():
                data_message += P + ": " + M[0].replace(".", '')
            data_errors['error'] = data_message
            return Response(data_errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CitationViewList(generics.ListAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (AllowAny,)
    queryset = Citations.objects.all()
    serializer_class = CitationsSerializer


#-----------------------------------------------------------------------------------------------------------
class ConnexionViewAdd(generics.CreateAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (AllowAny,)
    queryset = Connexion.objects.all()
    serializer_class = ConnexionSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data_errors = {}
            data_message = str('')
            for P, M in serializer.errors.items():
                data_message += P + ": " + M[0].replace(".", '')
            data_errors['error'] = data_message
            return Response(data_errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ConnexionViewList(generics.ListAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (AllowAny,)
    queryset = Connexion.objects.all()
    serializer_class = ConnexionSerializer

#----------------------------------------------------------------------------------------------------------

class MessagesViewAdd(generics.CreateAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (AllowAny,)
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data_errors = {}
            data_message = str('')
            for P, M in serializer.errors.items():
                data_message += P + ": " + M[0].replace(".", '')
            data_errors['error'] = data_message
            return Response(data_errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessagesViewList(generics.ListAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (AllowAny,)
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer

#-----------------------------------------------------------------------------------------------------------------------------
#from rest_framework.views import APIView
#from rest_framework.parsers import MultiPartParser, FormParser
#from rest_framework.response import Response
#from rest_framework import status

#from .serializers import FileSerializer

#class FileView(APIView):

#  parser_classes = (MultiPartParser, FormParser)

#  def post(self, request, *args, **kwargs):

#    file_serializer = FileSerializer(data=request.data)
#    if file_serializer.is_valid():
#      file_serializer.save()
#      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#    else:
#      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#from doac.contrib.rest_framework import authentication, permissions

#class ExampleViewSet(viewsets.ModelViewSet):
#    authentication_classes = [authentication.DoacAuthentication]
#    permissions_classes = [permissions.TokenHasScope]
#    model = ExampleModel
    
#    scopes = ["read", "write", "fun_stuff"]