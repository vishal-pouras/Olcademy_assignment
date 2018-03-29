"""Olcademy URL Configuration

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
from django.conf.urls import url
from team import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # To display the various teams
    path('teams/', views.teams, name='teams'),

    # To login as admin
    path('login/', views.login, name='login'),

    # To update the details of a particular team
    url(r'^adminpage/teams/update/(?P<pk>[0-9]+)$', views.TeamUpdate.as_view(), name='team-update'),

    # redirects to adminpage/teams/ {done to avoid Slash POST error}
    path('adminpage/', views.admin_redirect, name='admin-redirect'),

    # Admin page where all teams are displayed as List
    path('adminpage/teams/', views.TeamListView.as_view(), name='team-list'),

    # To add a new new team by admin
    path('adminpage/add/', views.TeamCreate.as_view(), name='team-add'),
]
