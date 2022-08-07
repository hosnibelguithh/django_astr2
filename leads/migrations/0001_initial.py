# Generated by Django 3.2 on 2022-07-14 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Prospect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=20)),
                ('Prénom', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('NumeroDeTelephone', models.CharField(max_length=20)),
                ('DDN', models.TimeField()),
                ('Marié', models.BooleanField(default=False)),
                ('NBEnfants', models.IntegerField(default=0)),
                ('Profession', models.CharField(max_length=20)),
                ('RevenuAnnuel', models.FloatField(default=0)),
                ('Adresse', models.CharField(max_length=20)),
                ('créeLe', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pas contacté', 'Pas contacté'), ('A relancer', 'A relancer'), ('En cours', 'En cours'), ('Pas intéressé', 'Pas intéressé'), ('Dossier Annulé', 'Dossier Annulé'), ('Converti', 'Converti')], default='Pas contacté', max_length=25)),
                ('Agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NatureDeVisite', models.TextField(choices=[('Evaluation', 'Evaluation'), ('Relance', 'Relance'), ('Vente', 'Vente'), ('RemiseDeContrat', 'RemiseDeContrat'), ('Recouvrement', 'Recouvrement')], default='Evaluation')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('Prospect', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.prospect')),
            ],
        ),
    ]