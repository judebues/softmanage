from django.urls import path
from django.conf.urls import url,include
from . import views
from rest_framework import routers
from secondtime import views

# router = routers.DefaultRouter()
# router.register(r'commdisaster',views.CommdisasterViewSet, basename='commdisaster')
# router.register(r'civilstructure',views.CivilstructureViewSet, basename='civilstructure')
# router.register(r'deathstatistics',views.DeathstatisticsViewSet, basename='deathstatistics')
# router.register(r'collapserecord',views.CollapserecordViewSet, basename='collapserecord')
# router.register(r'disasterprediction',views.DisasterpredictionViewSet, basename='disasterprediction')

urlpatterns = [ 
    url(r'^upload/$', views.upload_file),
    url(r"^download/$",views.download_file,name='down'),
    url(r"^index/$",views.home_page,name="home"),
    url(r"^search/$",views.search,name='search'),   
]