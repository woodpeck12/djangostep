"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

#from .views import hello,current_time,time_plus,contact,contact_thanks
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.hello),
    path('current_time/',views.current_time),
    path('time/plus/<int:plus>/',views.time_plus),
    path('',include('books.urls')),
    path('contact/',views.contact),
    path('contact/thanks/',views.contact_thanks),
]

