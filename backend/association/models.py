from django.db import models
from django.utils.text import slugify
from django.utils import timezone

from users.models import ProfileBenevole,User,ProfileAssociation
# Create your models here.





    


class Mission(models.Model):
        domaine_prefere = (
        ('Sport', 'Sport'),
        ('Santer', 'Santer'),
        ('Soutien Scolaire', 'Soutien Scolaire'),
        ('Aides Sociales', 'Aides Sociales'),
        ('Entreprenariat', 'Entreprenariat'),
        ('Informatique', 'Informatique'),
        ('Animation', 'Animation'),
      
        )
        nom=models.CharField(max_length=50,null=False,blank=False)
        description=models.CharField(max_length=150,null=False,blank=False) 
        date_publier=models.DateTimeField()  
        date_modification=models.DateTimeField(auto_now=True)
        date_fin=models.DateTimeField(default=timezone.now)
        domaine=models.CharField(max_length=20, choices=domaine_prefere)
        lieu=models.CharField(max_length=50,null=False,blank=False)
        nombre_participant=models.CharField(max_length=50,null=False,blank=False)
        photo_mission = models.ImageField( upload_to='uploads/images',null=True,blank=True)
        slug=models.SlugField(null=True,blank=True)
        association=models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)
        class Meta:
            ordering = ('-date_publier',)
            
        def save(self,*args, **kwargs):
            if not self.slug:
                self.slug=slugify(self.nom)
            super(Mission,self).save(*args, **kwargs)
        
        def __str__(self):
            return self.nom
       
        def fin_du_mission(self):
            return self.date_fin < timezone.now()
        


class Participer(models.Model):

    id_benevole =  models.CharField(max_length=150,null=False,blank=False)
    id_mission =  models.CharField(max_length=150,null=False,blank=False)
    participer = models.ForeignKey(Mission, on_delete=models.CASCADE,null=True,blank=True)
    # def __str__(self):
    def __str__(self):
            return self.id_mission


#ff5a