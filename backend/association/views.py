
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from users.models import ProfileBenevole,User

from users.models import ProfileAssociation
# from backend.users.models import ProfileAssociation, ProfileBenevole
from .forms import MissionForm, ParticiperForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.views.generic import  UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mission,Participer


def getLB(request):
    participerss=Participer.objects.filter()
    context={
        'participerss':participerss
    }
    print(participerss)
    return render(request, 'home/tst.html',context)

@login_required(login_url='login_user')
def association(request):  
    missions=Mission.objects.filter(association=request.user)

    if not missions.exists():
        messages.warning(request,'Aucun Mission Disponible')
    # mission=Mission.objects.all()
    # mission=Mission.objects.all()

    return render(request, 'home/Association.html', {
        'title': 'Association',
        'missions':missions,
        'mission':mission,
        

        # 'mission':mission
    })


@login_required(login_url='login_user')
def mission(request):
    # benevole=benevole.objects.all()

    if request.method=='POST':
        formm=MissionForm(request.POST,request.FILES)
        if formm.is_valid():
            instance=formm.save(commit=False)
            instance.association=request.user
            instance.save()
            return redirect('association')
    else:
        formm=MissionForm()
    return render(request, 'Association/mission.html', {
        'title': 'mission',
        'formm':formm,
    })

# def Participer(request):

#     #  if request.method=='POST':
#     #     forms=ParticiperForm(request.POST,request.FILES)
#     #     if forms.is_valid():
#     #         forms.save()
#     #         return redirect('association')
#     id_mission = Mission.objects.get(pk=id_mission)
#     id_benevole = Participer.objects.get(pk=id_benevole)
#     id_association = Participer.objects.get(pk=id_association)
#     participer = Participer.object.get(sulg=participer)
#     context={
#         'id_mission':id_mission,
#         'id_association':id_association,
#         'id_benevole':id_benevole
#     }
#     return render(request,'Accepter_refuser.html',{

#     },context)
    


def mission_detail(request,slug):
    mission= Mission.objects.get(slug=slug)
    return render(request, 'Association/mission_detail.html', {
        'title': 'mission',
        'mission':mission
    })




class mission_update(LoginRequiredMixin, UpdateView):
    model = Mission
    template_name = 'Association/mission_update.html'
    form_class = MissionForm
    success_url = '/association/'

class mission_delete(LoginRequiredMixin, DeleteView):
    model = Mission
    success_url = '/association/'

    
def benevole(request):
    missions=Mission.objects.all()
    return render(request, 'home/Benevole.html', {
        'title': 'Benevole',
        'missions':missions
    })
# def demande_participe(request,mission_id):
#     # demande_participe=False
#     # if demande_participe==True:
#     #     nbr_benevole_participe=nbr_benevole_participe+1
    
#     missions=Mission.objects.get(pk=mission_id) 
#     template=render_to_string('Association/email_template.html')
#     email=EmailMessage(     
#         'Veuillez confirmer  votre partiicipation a la mission prposer',#header message
#         template,#h1
#         settings.EMAIL_HOST_USER,
#         [request.user.email], 
#         )
#     email.fail_silenty=False
#     email.send()
    
#     return render(request,'Association/success.html',)

@login_required(login_url='login_user')
def ConfirmeParticipation(request,id):
    participers=Mission.objects.get(id=id)
    context = {
        "participers": participers,
    }

    template=render_to_string('Association/email_template.html',context=context)
    email=EmailMessage(
                'Veuillez confirmer  votre participation a la mission proposer',#header message
                template, # h1
                settings.EMAIL_HOST_USER,
                [request.user.email], 
                )
    email.fail_silenty=False
    email.send()
    return render(request,'Association/verf_email.html')


@login_required(login_url='login_user')
def demande_participer(request,id):
    participers=Mission.objects.get(id=id)



   
    benParticiper=User.objects.filter(username=request.user)

   
       
    return render(request,'Association/success.html', {'benParticiper':benParticiper,'participers':participers},)




def voirlistB(request,id):
    
    missions=Mission.objects.get(id=id)
    mission =Mission.objects.all()
    participers = Participer.objects.filter()
    context={
        'participers':participers
    }
    


 
 
   
   
   
   
    return render(request,'home/voirlistB.html',context)

def post(request):
    if request.method == 'POST':
        id_benevole = request.POST['nom_benevole']
        id_mission = request.POST['nom_mission']
        print("avant")
        print(id_benevole)
        print(id_mission)
        mission=Participer(id_benevole=id_benevole,id_mission=id_mission)
       
        mission.save()
        print("apres save")
        print(mission)
        print(id_benevole)
        print(id_mission)
    return render(request,'Association/success.html')


def accepter_association(request):
    accepter_par_admin=request.GET.get('accepter_par_admin')
    if accepter_par_admin==True:
        template=render_to_string('Association/email_template.html')
        email=EmailMessage(
                'Veuillez confirmer  votre participation a la mission proposer',#header message
                template, # h1
                settings.EMAIL_HOST_USER,
                [request.user.email], 
                )
        email.fail_silenty=False
        email.send()
    else:
        pass
    return render(request)
