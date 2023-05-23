from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
   
   
    path('registration/',views.registration,name='registration'),
    path('registerA/',views.registerA, name='registerA'),
    path('registerB/',views.registerB, name='registerB'),
    path('login/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('benevole/', views.benevole, name='benevole'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('Accept_refuser/', views.Accepte_refuser, name='Accept_refuser'),
    path('profileBenevole/',views.profileBenevole,name='profileBenevole'),
    path('profileBenUpdate/',views.profileBenUpdate,name='profileBenUpdate'),
    path('contactez_nous/',views.contactez_nous,name='contactez_nous'),
    path('profileAssociation/',views.profileAssociation,name='profileA'),
    path('profileAssUpdate/',views.profileAssUpdate,name='profileAssUpdate'),
    path('test/',views.test,name='test'),
    path('temoignage/',views.temoignage,name='temoignage'),
   

 


    # Reset Password

   
   

    # path('homeBenevole',views.homeben,name='homeben')
]