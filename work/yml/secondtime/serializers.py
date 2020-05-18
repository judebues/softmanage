from django.contrib.auth.models import User,Group
from rest_framework import serializers
from  .models import Commdisaster


class CommdisasterSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Commdisaster
        fields = ('id','date','location','type','grade','note','reportingunit')