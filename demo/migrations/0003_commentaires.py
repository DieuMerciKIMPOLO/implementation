# Generated by Django 2.0.1 on 2018-01-22 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_lesclientsoauth2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaires',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('commentaire', models.TextField(max_length=1000)),
                ('date_post', models.DateTimeField(auto_now_add=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
