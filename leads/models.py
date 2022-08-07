from django.db import models
from django.conf import settings
from django.urls import reverse

from datetime import datetime 



class Prospect(models.Model):
    PasContacte= 'Pas contacté'
    ARelancer = 'A relancer'
    EnCours = 'En cours'
    PasInteresse= 'Pas intéressé'
    DossierAnnule = 'Dossier Annulé'
    Signe = 'Signé'

    STATUS = (
        (PasContacte, 'Pas contacté'),
        (ARelancer, 'A relancer'),
        (EnCours, 'En cours'),
        (PasInteresse, 'Pas intéressé'),
        (DossierAnnule,'Dossier Annulé'),
        (Signe,'Signé'),
    )

    Nom = models.CharField(max_length=20)
    Prénom = models.CharField(max_length=20)
    Email = models.EmailField()
    NumeroDeTelephone = models.CharField(max_length=20)
    Age = models.IntegerField(default=0)
    Marié = models.BooleanField(default=False)
    NBEnfants = models.IntegerField(default=0)
    Agent = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, on_delete=models.SET_NULL)
    Profession = models.CharField(max_length=20)
    RevenuAnnuel = models.FloatField(default=0)
    Adresse = models.CharField(max_length=20)
    
    créeLe = models.DateField(auto_now_add=True)
    
    status = models.CharField(max_length=25, choices=STATUS, default=PasContacte)

    def __str__(self):
        return f"{self.Nom} {self.Prénom}"


class Event(models.Model):
    Evaluation = 'Evaluation'
    Relance = 'Relance'
    Vente = 'Vente'
    RemiseDeContrat = 'RemiseDeContrat'
    Recouvrement = 'Recouvrement'

    NATURE = (
        (Evaluation, 'Evaluation'),
        (Relance,'Relance'),
        (Vente, 'Vente'),
        (RemiseDeContrat, 'RemiseDeContrat'),
        (Recouvrement,'Recouvrement'),
    )

    Intéressé = 'Intéressé'
    NonIntéressé = 'NonIntéressé'
    ARevoir = 'A revoir'
    FixationDeRDV= 'FixationDeRDV'
    Recommandation= 'Recommandation'

    RESULTATS = (
        (Intéressé, 'Intéressé'),
        (NonIntéressé,'NonIntéressé'),
        (ARevoir, 'A revoir'),
        (RemiseDeContrat, 'RemiseDeContrat'),
        (Recommandation,'Recommandation'),
    )

    
    
    Prospect = models.ForeignKey(Prospect,null=True, on_delete=models.CASCADE)

    NatureDeVisite = models.TextField(choices=NATURE, default=Evaluation, blank=False)
    ResultatDeVisite = models.TextField(choices=RESULTATS, default=Evaluation, blank=False)



    DateDeProspection = models.DateField(default=datetime.now())

    Proposition = models.BooleanField(default=False, blank= True)
        
    PerformanceRetraitePlus = 'Performance Retraite Plus'
    MixteSimple = 'Mixte simple'
    MixteDynamique = 'Mixte Dynamique'
    RenteEducation= 'Rente Education'
    CapitalisationIndividuelle= 'Capitalisation Individuelle'
    TYPES = (
        (PerformanceRetraitePlus, 'Performance Retraite Plus'),
        (MixteSimple,'Mixte Simple'),
        (MixteDynamique, 'Mixte Dynamique'),
        (RenteEducation, 'Rente Education'),
        (CapitalisationIndividuelle,'Capitalisation Individuelle'),
    )
    TypeContratOffert = models.TextField(choices=TYPES, blank=True)

    DureeContratOffert = models.IntegerField(default=0, blank=True)





    
   


    

    


