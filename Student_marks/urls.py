"""
URL configuration for Student_marks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Application1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('homepage/',views.home_page,name='homepage'),
    path('registration/',views.reg,name='reg'),
    path('login/',views.login,name='login'),
    path('save/',views.save,name='save'),
    path('success/',views.success,name='success'),
    path('logi',views.logi,name='logi'),
    path('dash',views.dashboard,name='dashboard')
]
