from asyncio.windows_events import NULL
from contextlib import nullcontext
from email.mime import image
from imp import NullImporter
from multiprocessing import context
from queue import Empty

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login , authenticate, logout

from  association.models import Mission,Participer
from .forms import UserForm,BenevoleForm,AssociationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required




from .models import ProfileAssociation,User,ProfileBenevole,Temoignages

# # Create your views here.



def home(request):
    mission=Mission.objects.all()
    temoignage=Temoignages.objects.all()
    countB=ProfileBenevole.objects.all().count()
    countA=ProfileAssociation.objects.all().count()
    countM=Mission.objects.all().count()
    context={
        'countB':countB,
        'countA':countA,
        'countM':countM,
        'mission':mission,
        'temoignage':temoignage
    }

    return render(request,'home/index.html',context)

def temoignage(request):
    # benevole_T=Temoignages.objects.all()
    benevole_T=User.objects.filter(username=request.user)
    if request.method=='POST':
        nom=request.POST['nom']
        message=request.POST['message']
        tem=Temoignages(nom=nom,message=message)
        tem.save()
        return redirect('benevole')
    
    return render(request, 'home/Temoignage.html', {'title':'Temoignage','benevole_T':benevole_T})

def about(request):
    return render(request,'home/homeAssociation.html')

def registration(request):
     return render(request,'registration/password_reset_complete.html')



        
def logout_user(request):
    logout(request)
    return render(request,'home/logout.html',{'title':'Deconnexion'})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.est_association:
                return redirect('association')
            else:
                return redirect('benevole')

        else:
            messages.warning(
                request, 'Il y a une erreur dans le nom dutilisateur ou le mot de passe.')

    return render(request, 'home/login.html', {
        'title': 'Se Connecter',
    })



def Accepte_refuser(request):

    try:
        benevoles=ProfileBenevole.objects.get(user=request.user)
    except Exception as e:
        benevoles=None
        print('Exception :',e)

    context={
        'benevoles':benevoles,
        
    }
    
    return render(request, 'home/Accept_refuser.html',context)
    
# def post(request):
#     nomComplet = request.GET['nomComplet']
#     return render(request, 'home/post.html',{"result":nomComplet})
   


def registerA(request):
    if request.method == 'POST':
    #variable for fields :
        logo =request.FILES['logo']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        nom_association = request.POST['nom_association']
        nom_complet =request.POST['nom_complet']
        telephone = request.POST['telephone']
        description = request.POST['description']
        adresse = request.POST['adresse']
        ville = request.POST['ville']
        nbr_membre_bureau = request.POST['nbr_membre_bureau']
        nbr_beneficiere =request.POST['nbr_beneficiere']
        siteweb =request.POST['siteweb']
        activiter_prefere  =request.POST['activiter_prefere']
        if User.objects.filter(username=username).exists():
            messages.warning(request,'votre username est exist déja !!!')
        
        elif password1!=password2:
            messages.warning(request,'votre mot de passe et le mot de passe de confirmation ne correspondent pas')
            



        else:
          
            
         # add new user:

            user=User.objects.create_user(username=username,
                                          email=email,
                                          password1=password1,
                                          password2=password2)
            user.est_association = True
            user.set_password(request.POST['password1'])

            user.save()
            # add association
            association=ProfileAssociation(user=user,
                    logo=logo,
                    adresse=adresse,activiter_prefere=activiter_prefere,
                    nbr_beneficiere=nbr_beneficiere,
                    nbr_membre_bureau=nbr_membre_bureau,description=description,
                    siteweb=siteweb,telephone=telephone,ville=ville,
                    nom_association=nom_association,nom_complet=nom_complet)
            # clear fields:
            logo =''
            username = ''
            email = ''
            password1 = ''
            password2 = ''
            nom_association = ''
            nom_complet =''
            telephone = ''
            description = ''
            adresse = ''
            ville = ''
            nbr_membre_bureau = ''
            nbr_beneficiere =''
            siteweb =''
            activiter_prefere  =''
            association.save()
            # Success messages
            
            messages.success(request,'Votre Compte est Creer avec Succeer')
            return redirect('login_user')
    return render(request, 'home/registerA.html', {
        'title': 'التسجيل',
    })
    

def registerB(request):
    if request.method == 'POST':
        #variable for fields :
        photo_profile =request.FILES['photo_profile']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        nomComplet = request.POST['nomComplet']
        genre = request.POST['genre']
        telephone =request.POST['telephone']
        adresse = request.POST['adresse']
        ville = request.POST['ville']
        date_naissance = request.POST['date_naissance']
        cin = request.POST['cin']
        domaine_experience = request.POST['domaine_experience']
        biographie =request.POST['biographie']
        activiter_prefere =request.POST['activiter_prefere']
        if User.objects.filter(username=username).exists():
            messages.warning(request,'votre username est exist déja !!!')
        elif password1!=password2:
            messages.warning(request,'votre mot de passe et le mot de passe de confirmation ne correspondent pas')

        elif photo_profile is None:         
               messages.warning(request,'Votre Photo de Profile est  Vide !!!')
        else:
         # add new user:

            user=User.objects.create_user(username=username,email=email,password1=password1,password2=password2)
            user.est_benevolat = True
            user.set_password(request.POST['password1'])
            user.save()
            # add benevole
            benevole=ProfileBenevole(user=user,
                photo_profile=photo_profile,
                nomComplet=nomComplet,activiter_prefere=activiter_prefere,
                domaine_experience=domaine_experience,
                cin=cin,adresse=adresse,
                genre=genre,
                telephone=telephone,ville=ville,date_naissance=date_naissance,biographie=biographie)
            # clear fields:
            photo_profile =''
            username = ''
            email = ''
            password1 = ''
            password2 = ''
            nomComplet = ''
            telephone = ''
            adresse =''
            genre=''
            ville = ''
            date_naissance = ''
            cin = ''
            domaine_experience = ''
            biographie =''
            activiter_prefere  =''
            benevole.save()
            # Success messages
            messages.success(request,'Votre Compte est créé avec Succès')
            return redirect('login_user')
    return render(request, 'home/registerB.html', {
        'title': 'التسجيل' ,  
    })


def benevole(request):
   
    return render(request, 'home/Benevole.html', {
        'title': 'Benevole',
    })

def profileBenevole(request):
        benevole= ProfileBenevole.objects.all()
        
        return render(request,'Association/profile.html',{'benevole':benevole})
    




def profileBenUpdate(request):
    if request.method=='POST':
        user_form=UserForm(request.POST,instance=request.user)
        profile_form=BenevoleForm(request.POST,request.FILES,instance=request.user.benevole)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Le profil a été mis à jour.')
            return redirect('profileBenevole')
    else:
        user_form=UserForm(instance=request.user)
        profile_form=BenevoleForm(instance=request.user.benevole)
    context={
            'title':'Update Profile',
            'user_form':user_form,
            'profile_form':profile_form
    }
    return render(request,'Association/profile_update.html',context)


def contactez_nous(request):
    
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        print(subject)
        print(email)
        print(message)
        
        send_mail(subject,
                  message,
                  settings.EMAIL_HOST_USER,
                  ['othmane.boudali01@gmail.com',email], fail_silently=False)
    return render(request, 'home/contact.html', {})


@login_required(login_url='login_user')
def profileAssociation(request):
        association= ProfileAssociation.objects.all()
        
        return render(request,'Association/ProfileAssociation.html',{'association':association})

def profileAssUpdate(request):
    if request.method=='POST':
        user_form=UserForm(request.POST,instance=request.user)
        profile_form=AssociationForm(request.POST,request.FILES,instance=request.user.association)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Le profil a été mis à jour.')
            return redirect('profileA')
    else:
        user_form=UserForm(instance=request.user)
        profile_form=AssociationForm(instance=request.user.association)
    context={
            'title':'Update Profile',
            'user_form':user_form,
            'profile_form':profile_form
    }
    return render(request,'Association/profileAss-update.html',context)

def test(request):
    association=ProfileAssociation.objects.all()
    benevole=ProfileBenevole.objects.all()
    association_no=association.count()
    benevole_no=benevole.count()
    mission_no=Mission.objects.all().count()
    benevole_homme=ProfileBenevole.objects.filter(genre="HOMME").count()
    benevole_femme=ProfileBenevole.objects.filter(genre="FEMME").count()
    top_ville=ProfileBenevole.objects.filter(ville="Casablanca")
    ville_t=top_ville.count()
    context={
        'association':association,
        'benevole':benevole,
        'association_no':association_no,
        'benevole_no':benevole_no,
        'mission_no':mission_no,
        'benevole_homme':benevole_homme,
        'benevole_femme':benevole_femme,
        'ville_t':ville_t
        
    }
    return render(request,'home/test.html',context)