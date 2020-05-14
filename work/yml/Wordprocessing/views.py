from django.shortcuts import render
from django.http import HttpResponse
from .models import Commdisaster
from django.forms.models import model_to_dict
from .serializers import CommdisasterSerializers
from rest_framework import viewsets
import os

result = Commdisaster.objects.values()
# Create your views here.
def home_page(request):
    # print(type(result))
    # result_list = [ item for item in result]
    return render(request,'index.html',{'info':result})

# search info according the request
# def search_info(request):


def upload_file(request):
    # 请求方法为PO
    # ST时，进行处理
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，则默认为None
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("没有需要上传的文件")
        else:
            absdir = os.path.dirname(os.path.abspath(__file__))
            #打开特定的文件进行二进制的写操作
            try:
                with open(absdir+"/static/filestore/%s" % File.name, 'wb+') as f:
                    #分块写入文件
                    for chunk in  File.chunks():
                        f.write(chunk)
                return HttpResponse("UPload over!")
            except FileNotFoundError as e:
                print(e)
                print('**************')


    else:
        return  render(request, "index.html",{'info':result})
    

class CommdisasterViewSet(viewsets.ModelViewSet):
    queryset = Commdisaster.objects.all()
    serializer_class = CommdisasterSerializers