"""yml URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Wordprocessing import views
from django.conf.urls import url,include
from rest_framework import routers
from secondtime import views

router = routers.DefaultRouter()
router.register(r'commdisaster',views.CommdisasterViewSet, basename='commdisaster')
router.register(r'commdisaster',views.CommdisasterViewSet, basename='commdisaster')
router.register(r'civilstructure',views.CivilstructureViewSet, basename='civilstructure')
router.register(r'deathstatistics',views.DeathstatisticsViewSet, basename='deathstatistics')
router.register(r'collapserecord',views.CollapserecordViewSet, basename='collapserecord')
router.register(r'disasterprediction',views.DisasterpredictionViewSet, basename='disasterprediction')



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/',include(router.urls)),
    url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^',include('Wordprocessing.urls')),
    url(r'^fileupload/',include('fileupload.urls')),
    url(r'^secondtime/',include('secondtime.urls')),
]   

