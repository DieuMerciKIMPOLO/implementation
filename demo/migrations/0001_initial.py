# Generated by Django 2.0.1 on 2018-01-04 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profilutilisateur',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nom_utilisateur', models.CharField(max_length=300, unique=True)),
                ('prenom', models.CharField(max_length=300)),
                ('nom', models.CharField(max_length=300)),
                ('is_active', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_inscription', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Citations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('citation', models.TextField(max_length=1000)),
                ('auteur', models.CharField(max_length=100)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Connexion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_demande', models.DateTimeField(auto_now_add=True)),
                ('date_confirmation', models.DateTimeField(auto_now_add=True)),
                ('statu_de_connexion', models.BooleanField(default=False)),
                ('utilisateur_confirmateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connexion_utilisateur_confirmateur', to=settings.AUTH_USER_MODEL)),
                ('utilisateur_demandeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connexion_utilisateur_demandeur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_envoi', models.DateTimeField(auto_now_add=True)),
                ('statu_de_message', models.BooleanField(default=False)),
                ('utilisateur_expediteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_utilisateur_expediteur', to=settings.AUTH_USER_MODEL)),
                ('utilisateur_recepteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_utilisateur_recepteur', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoleUtilisateur',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.IntegerField(choices=[(1, 'Client'), (2, 'Fournisseur'), (3, 'Partenaire'), (4, 'Responsable')], default=1)),
                ('statu_du_role', models.BooleanField(default=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
