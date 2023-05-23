from  django import forms
from .models import ProfileBenevole,User,ProfileAssociation
# from .models import Association
# class AssociationFormAdmin(forms.ModelForm):
#     class Meta:
#         model = Association
#         fields = '_all_'
#     def status(self):
#         if self.accepter_par_admin == True:
#                 self.status = 'Accepter'
#                 self.save()
#         else:
#             # raise forms.ValidationError("No Vampires")
#             self.status = 'Refuser'
#             self.save()
#         return self.cleaned_data["status"]
#     # @property
#     # def accepter_association(self):
#     #         if not self.accepter_par_admin:
#     #             self.accepter_par_admin = True




#     # @property
#     # def attente_association(self):
#     #         if self.accepter_par_admin:
#     #             self.accepter_par_admin = False
#     #             self.status = 'en Attente'
#     #             self.save()




#     # @property
#     # def refuser_association(self):
#     #         if self.accepter_par_admin or not self.accepter_par_admin:
#     #             self.accepter_par_admin = False
               
               



        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
           'username',
            'email',
            'password1',
            'password2',
        ]

class BenevoleForm(forms.ModelForm):
    class Meta:
        model = ProfileBenevole
        fields = [
        'photo_profile',
        'nomComplet',
        'telephone',
        'adresse',
        'date_naissance',
        'cin',
        'domaine_experience',
        'ville',
        'biographie',
        'activiter_prefere',
        ]

class AssociationForm(forms.ModelForm):
    class Meta:
        model = ProfileAssociation
        fields = [
        'logo',
        'nom_association',
        'nom_complet',
        'telephone',
        'description',
        'adresse',
        'ville',
        'nbr_membre_bureau',
        'nbr_beneficiere',
        'siteweb',
        'activiter_prefere',
        ]