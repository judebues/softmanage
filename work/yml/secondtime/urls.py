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
    url(r'^uploadfile/$', views.uploadfile),
    url(r'^upload/$',views.upload),
    url(r"^download/$",views.download_file,name='down'),
    url(r"^index/$",views.home_page,name="home"),
    url(r"^Commdisaster/$",views.commdisaster), 
    url(r"^Deathstatistics/$",views.deathstatistics), 
    url(r"^Disasterprediction/$",views.disasterprediction), 
    url(r"^Collapserecord/$",views.collapserecord), 
    url(r"^Civilstructure/$",views.civilstructure), 
    # url(r"^search/$",views.search), 
    url(r'^delete_Comm/(\w+)/$',views.delete_Comm,name='delete_Comm'),
    url(r'^delete_death/(\w+)/$',views.delete_death,name='delete_death'),
    url(r'^delete_civil/(\w+)/$',views.delete_civil,name='delete_civil'),
    url(r'^delete_colla/(\w+)/$',views.delete_colla,name='delete_colla'),
    url(r'^delete_request/(\w+)/$',views.delete_request,name='delete_request'),
    url(r'^update_sendrecode/(\w+)/$',views.updatesendrecode,name='update_sendrecode'),
    url(r"^sendlist/$",views.sendlist), 
    url(r"^sign_in/$",views.sign_in), 
    url(r"^sign_up/$",views.sign_up), 
    

    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^captcha/', include('captcha.urls')),

    # url(r'^sendlist/$',views.sendlist),
    url(r'^send/$',views.send,name="send"),
    url(r'^sendinfo/$',views.sendinfo,name="sendinfo"),
]