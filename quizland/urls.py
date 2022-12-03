from django.urls import path
from . import views
from .views import QuizDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path('/<slug:slug>/', QuizDetailView.as_view(), name='quiz-detail'),


    #path('literature/', views.lit, name='lit'),
   # path('geo/', views.geo, name='geo'),
    #path('languages/', views.lang, name='languages'),
 #   path('basic/', views.basic, name='basic'),
  #  path('science/', views.science, name='science'),
]