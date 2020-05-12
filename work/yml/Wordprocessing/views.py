from django.shortcuts import render
from django.http import HttpResponse
from .models import Commdisaster
from django.forms.models import model_to_dict
from .serializers import CommdisasterSerializers
from rest_framework import viewsets

# Create your views here.
def home_page(request):
    result = Commdisaster.objects.values()
    # print(type(result))
    print(result)
    # result_list = [ item for item in result]
    return render(request,'index.html',{'info':result})


class CommdisasterViewSet(viewsets.ModelViewSet):
    queryset = Commdisaster.objects.all()
    serializer_class = CommdisasterSerializers