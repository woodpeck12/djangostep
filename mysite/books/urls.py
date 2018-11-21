
from django.urls import path

from books import views

urlpatterns = [
    path('search_form/', views.search_form),
    path('search/', views.search),

]
