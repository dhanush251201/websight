"""Webinar_webapp URL Configuration

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
from webinar import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_views.logout, name='logout'),
    path('delete/', user_views.deleteAccount, name='delete'),
    path('categories/',views.categories, name='categories'),
    path('art/',views.art, name='art'),
    path('architecture/',views.architecture, name='architecture'),
    path('business/',views.business, name='business'),
    path('contentwriting/',views.contentwriting, name='contentwriting'),
    path('cooking/',views.cooking, name='cooking'),
    path('dance/',views.dance, name='dance'),
    path('gardening/',views.gardening, name='gardening'),
    path('photography/',views.photography, name='photography'),
    path('technology/',views.technology, name='technology'),
    path('settings/',user_views.userSettings, name='settings'),
    path('profile/',user_views.profile, name='profile'),
    path('', include('webinar.urls'), name='webinar-home'),
]
