from django.db import models
from django.utils import timezone
# from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save



class  User(AbstractUser):
    est_association = models.BooleanField(default=False)
    est_benevolat = models.BooleanField(default=False)
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField()
    password1 = models.CharField(max_length=20,null=True)
    password2 = models.CharField(max_length=20,null=True)
class ProfileAssociation(models.Model):
    nbr_bureau = [
        ('- Choisir une valeur -', '- Choisir une valeur -'),
        ('de 0 a 5', 'de 0 a 5'),
        ('de 5 a 10', 'de 5 a 10'),
        ('de 10 a plus', 'de 10 a plus'),

    ]
    nbr_beneficier = [
        ('- Choisir une valeur -', '- Choisir une valeur -'),
        ('0 a 50', '0 a 50'),
        ('50 a  plus', '50 a  plus'),

    ]
    activiter_prefere = (
        ('Sport', 'Sport'),
        ('Santer', 'Santer'),
        ('Education', 'Education'),
        ('Enseignement', 'Enseignement'),
        ('Entreprenariat', 'Entreprenariat'),
        ('Protection de lenvironnement', 'Protection de lenvironnement'),
        ('Handicap', 'Handicap'),
        ('Droits de la femme', 'Droits de la femme'),
        ('Autres Domaine', 'Autres Domaine'),
      
        )
   
    logo = models.ImageField( upload_to='uploads/images',null=True,blank=True)
    user = models.OneToOneField(User,related_name="association",on_delete = models.CASCADE, primary_key = True)
    nom_association = models.CharField(max_length=50)
    nom_complet = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20,null=True, blank=False)
    description = models.TextField(max_length=200,null=True)
    adresse = models.TextField(max_length=100,null=True,blank=True)
    ville = models.CharField(max_length=30,null=True, blank=False)
    nbr_membre_bureau = models.CharField(
        max_length=25, choices=nbr_bureau, default='- Choisir une valeur -')
    nbr_beneficiere = models.CharField(
        max_length=25, choices=nbr_beneficier, default='- Choisir une valeur -')
    siteweb = models.CharField(max_length=40,null=True)
    activiter_prefere  = models.CharField(max_length=100, choices=activiter_prefere)
    accepter_par_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

class ProfileBenevole(models.Model):
    ville = [
        ('--Aucun--', '--Aucun--'),
        ('Agadir', 'Agadir'),
        ('Casablanca', 'Casablanca'),
        ('Essaouira', 'Essaouira'),
        ('Fes', 'Fes'),
        ('Marrakech', 'Marrakech'),
        ('Meknes', 'Meknes'),
        ('Oujda', 'Oujda'),
        ('Rabat', 'Rabat'),
        ('Tanger', 'Tanger'),
        ('Tetouan', 'Tetouan'),

    ]
    activiter_prefere = (
        ('Cadre', 'Cadre'),
        ('Salarié', 'Salarié'),
        ('Sans emploi', 'Sans emploi'),
        ('Commercent', 'Commercent'),
        ('Etudiant', 'Etudiant'),
        ('Autre', 'Autre'),
      
        )
    genre=(
        ('--Aucun--','--Aucun--'),
        ('FEMME','FEMME'),
        ('HOMME','HOMME'),
    )
    user = models.OneToOneField(User,related_name="benevole", on_delete = models.CASCADE, primary_key = True)
    photo_profile = models.ImageField( upload_to='uploads/images',null=True,blank=True)
    nomComplet = models.CharField(max_length=50,null=True)
    telephone = models.CharField(max_length=20,null=True)
    adresse = models.CharField(max_length=100,null=True)
    genre = models.CharField(max_length=100, choices=genre,default='--Aucun--')
    ville = models.CharField(max_length=20, choices=ville, default='--Aucun--')
    date_naissance = models.DateTimeField(default=timezone.now)
    cin = models.CharField(max_length=12, null=True)
    domaine_experience = models.TextField(null=True)
    biographie = models.TextField(null=True, blank=False)
    activiter_prefere  = models.CharField(max_length=100, choices=activiter_prefere)
    def __str__(self):
        return self.user.username

class Temoignages(models.Model):
    nom=models.CharField(max_length=100,null=True,blank=True)
    message=models.TextField(max_length=200,null=True,blank=True)
    def _str_(self):
        return str(self.nom)