from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from oauth2_provider.models import AbstractApplication
#from .manager import UserManager
#from django.contrib.auth.models import PermissionsMixin
import uuid
ROLES=(
	(1, 'Client'),
	(2, 'Fournisseur'),
	(3, 'Partenaire'),
	(4, 'Responsable')
	)
class UserManager(BaseUserManager):
	"""UserManager"""
	def _create_user(self, nom_utilisateur, password, **extera_fields):
		if not nom_utilisateur:
			raise ValueError("Le nom d' utilisateur est obligatoire")
		if not password:
			raise ValueError("Le mode de passe d' utilisateur est obligatoire")

		utilisateur=self.model(nom_utilisateur=nom_utilisateur, **extera_fields)
		utilisateur.set_password(password)
		utilisateur.save(using=self._db)
		return utilisateur

	def create_user(self, nom_utilisateur, password=None, **extera_fields):
		extera_fields.setdefault('is_superuser', False)
		return self._create_user(nom_utilisateur, password, **extera_fields)

	def create_superuser(self, nom_utilisateur, password, **extera_fields):
		extera_fields.setdefault('is_superuser', True)
		extera_fields.setdefault('is_staff', True)
		extera_fields.setdefault('is_active', True)
		if extera_fields.get('is_superuser') is not True:
			raise ValueError('Les super utilisateurs doivent avoir l attribut is_superuser=True')
		return self._create_user(nom_utilisateur, password, **extera_fields)

class Profilutilisateur(AbstractBaseUser):
	"""profils des utilisateurs"""
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	nom_utilisateur = models.CharField(max_length=300, unique=True)
	prenom = models.CharField(max_length=300)
	nom= models.CharField(max_length=300)
	is_active = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_staff= models.BooleanField(default=False)
	date_inscription= models.DateTimeField(auto_now_add=True)

	objects= UserManager()

	USERNAME_FIELD='nom_utilisateur'
	REQUIRED_FIELDS=['prenom','nom']

	def has_perm(self, perm, obj=None):
		return self.is_superuser

	def has_module_perms(self, app_label):
		return self.is_superuser

	def get_short_name(self):
		pass
	def __str__(self):
		return self.nom_utilisateur
	#def save(self, *args, **kwargs):
	#	self.set_password(self.password)
	#    super(Post, self).save(*args, **kwargs)


		
class RoleUtilisateur(models.Model):
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	utilisateur=models.ForeignKey(Profilutilisateur, on_delete=models.CASCADE)
	role=models.IntegerField(choices=ROLES, default=1)
	statu_du_role=models.BooleanField(default=True)
	date_creation=models.DateTimeField(auto_now_add=True)


class Citations(models.Model):
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	utilisateur=models.ForeignKey(Profilutilisateur, on_delete=models.CASCADE)
	citation=models.TextField(max_length=1000)
	auteur=models.CharField(max_length=100)

class Commentaires(models.Model):
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	utilisateur=models.ForeignKey(Profilutilisateur, on_delete=models.CASCADE)
	commentaire=models.TextField(max_length=1000)
	date_post=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.utilisateur)

class Connexion(models.Model):
	"""connexion"""
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	utilisateur_demandeur=models.ForeignKey(Profilutilisateur, on_delete=models.CASCADE, related_name='connexion_utilisateur_demandeur')
	utilisateur_confirmateur= models.ForeignKey(Profilutilisateur, on_delete=models.CASCADE, related_name='connexion_utilisateur_confirmateur')
	date_demande=models.DateTimeField(auto_now_add=True)
	date_confirmation=models.DateTimeField(auto_now_add=True)
	statu_de_connexion=models.BooleanField(default=False)

class Messages(models.Model):
	"""Messages"""
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	utilisateur_expediteur=models.ForeignKey(Profilutilisateur, on_delete=models.CASCADE, related_name='message_utilisateur_expediteur')
	utilisateur_recepteur= models.ForeignKey(Profilutilisateur, on_delete=models.CASCADE, related_name='message_utilisateur_recepteur')
	date_envoi=models.DateTimeField(auto_now_add=True)
	statu_de_message=models.BooleanField(default=False)


class LesClientsOauth2(AbstractApplication):
   logo_app = models.FileField(blank=True, null=False)
   descrip = models.TextField(max_length=1000)

   def allow_grant_type(self, *grant_types):
   	return bool(set(self.authorization_grant_type, self.GRANT_CLIENT_CREDENTIALS)&grant_types)

#     #models.CharField(max_length=1000)
