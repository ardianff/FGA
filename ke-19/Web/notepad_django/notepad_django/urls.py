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

from notepad.views import list_data, create, remove, view, edit

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('lihat/<int:get_id>', view, name='url_view'),                      
    path('buat/', create, name='url_create'),
    path('hapus/<int:get_id>', remove, name='url_remove'),
    path('edit/<int:get_id>', edit, name='url_edit'),
    path('', list_data, name='url_list')    
]
