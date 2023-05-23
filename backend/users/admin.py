from django.contrib import admin
from .models import *

# Register your models here.
class AssociationAdmin(admin.ModelAdmin):
    site_header= ("Benevolat Admin"),
    site_title= ("Admin"),
 
    search_fields=['nom_association']
    list_filter= ('accepter_par_admin',)

class BenevoleAdmin(admin.ModelAdmin):
    site_header= ("Benevolat Admin"),
    site_title= ("Admin"),
    search_fields=['nomComplet']


admin.site.register(User)
admin.site.register(ProfileAssociation,AssociationAdmin)
admin.site.register(ProfileBenevole,BenevoleAdmin)
admin.site.register(Temoignages)

