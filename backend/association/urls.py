from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('mission/',views.mission,name='mission'),
    path('', views.association, name='association'),
    path('mission_detail/<slug:slug>/', views.mission_detail, name='mission_detail'),
    path('mission_detail/<slug:slug>/update/', views.mission_update.as_view(), name='mission_update'),
    path('mission_detail/<slug:slug>/delete/', views.mission_delete.as_view(), name='mission_delete'),
    path('benevole/', views.benevole, name='benevole'),
    path('benevole/demande_participer/<int:id>/', views.demande_participer, name='demande_participer'),
    path('participer/',views.Participer,name="participer"),
    path('post/',views.post,name='post'),
    path('voirlistB/<int:id>/',views.voirlistB,name="voirlistB"),
    path('ConfirmeParticipation/<int:id>/',views.ConfirmeParticipation,name="ConfirmeParticipation"),
    # path('getLB',views.getLB, name="getLB"),
    path('tst/',views.getLB, name="tst")
 
   


] 