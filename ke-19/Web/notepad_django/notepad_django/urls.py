"""notepad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from notepad.views import notepad_list, notepad_create, notepad_remove, notepad_view, notepad_edit

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('lihat/<int:pk>', notepad_view, name='url_view'),                      
    path('buat/', notepad_create, name='url_create'),
    path('hapus/<int:pk>', notepad_remove, name='url_remove'),
    path('edit/<int:pk>', notepad_edit, name='url_edit'),
    path('', notepad_list, name='url_list')    
]
