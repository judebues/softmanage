from django.contrib.auth.models import User,Group
from rest_framework import serializers
from  .models import Commdisaster,Civilstructure,Deathstatistics,Commdisaster,Collapserecord,Disasterprediction,Disasterrequest


class CommdisasterSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Commdisaster
        fields = ('id','date','location','type','grade','note','reportingunit')

class CivilstructureSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Civilstructure
        fields = ('id','date','location','basicallyintactsquare','damagedsquare','distoryedsquare','note','reportingunit')

class DeathstatisticsSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deathstatistics
        fields = ('id','date','location','number','reportingunit')

# class CommdisasterSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Civilstructure
#         fields = ('id','date','location','type','grade','note','reportingunit')


class CollapserecordSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collapserecord
        fields = ('id','date','location','type','status','note','reportingunit')

class DisasterpredictionSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disasterprediction
        fields = ('id','date','location','longitude','latitude','depth','magnitude','intensity','type','status','note','reportingunit')

class DisasterrequestSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Civilstructure
        fields = ('id','date','disastertype','status','o_url','reportingunit')


