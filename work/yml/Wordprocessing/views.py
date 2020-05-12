from django.shortcuts import render
from django.http import HttpResponse
from .models import Commdisaster
from django.forms.models import model_to_dict

# Create your views here.
def home_page(request):
    result = Commdisaster.objects.values()
    # print(type(result))
    print(result)
    # result_list = [ item for item in result]
    return render(request,'index.html',{'info':result})