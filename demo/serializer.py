#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from demo.models import *


class ProfilutilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profilutilisateur
        fields=('nom','prenom','nom_utilisateur','password')
        #exclude = ('is_superuser','is_staff','is_active')
    def create(self, validated_data):
        profil = Profilutilisateur(
            nom_utilisateur=validated_data['nom_utilisateur'],
            nom=validated_data['nom'],
            prenom=validated_data['prenom']
        )
        profil.set_password(validated_data['password'])
        profil.save()
        return profil

        
class ProfilutilisateurListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profilutilisateur
        fields = ('nom','prenom', 'nom_utilisateur')

class RoleUtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleUtilisateur
        fields = '__all__'

class CommentairesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaires
        fields = '__all__'

class CommentairesAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaires
        exclude = ('utilisateur','date_post')

class CitationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citations
        fields = '__all__'


class ConnexionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connexion
        fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'