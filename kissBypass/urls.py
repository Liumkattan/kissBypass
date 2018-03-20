"""kissBypass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from imageDatabase import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ImageHashView.as_view(), name='list all'),
    path('<str:image_hash>', views.ImageWordsView.as_view(), name='hash lockup'),
    path('hash/', views.HashView.as_view(), name='list hash'),
    path('new/', views.InputView.as_view(), name='add image')
]
