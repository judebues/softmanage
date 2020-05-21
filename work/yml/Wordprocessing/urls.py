from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [ 
    url(r'^upload/$', views.upload_file),
    url(r"^download/$",views.download_file,name='down'),
    url(r"^index/$",views.home_page,name="home"),
    url(r"^search/$",views.search,name='search'),   
]