from tkinter import Widget
from django import forms
from .models import Mission,Participer





class MissionForm(forms.ModelForm):

     class Meta:
        model = Mission
        fields = ['nom','description','date_publier','date_fin',
                'domaine','lieu','nombre_participant',
                'photo_mission',]
        
        
class ParticiperForm(forms.ModelForm):
        class Meta:
                model = Participer
                fields ='__all__' 

        

        