from django.shortcuts import render
from django.http import HttpResponse
from .models import Commdisaster
from django.forms.models import model_to_dict
from .serializers import CommdisasterSerializers
from rest_framework import viewsets
import os,json
from .models import Commdisaster
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def home_page(request):
    # print(type(result))
    # result_list = [ item for item in result]
    result = Commdisaster.objects.values()
    return render(request,'index.html',{'info':result})

# search info according the request
# def search_info(request):
def search(request):
    if request.method == "POST":
        search_code = request.POST.get('search')
        if 1<len(search_code)<19:
            return HttpResponse("数据格式输入错误，请重新输入")
        elif len(search_code) < 1:
            result = Commdisaster.objects.values()
        else:
            result = Commdisaster.objects.filter(id=search_code)
    return render(request,'index.html',{'info':result})


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
                writeToDb(absdir+"/static/filestore/%s" % File.name)
                return HttpResponse("UPload over!")
            except FileNotFoundError as e:
                print(e)
                return HttpResponse("no error")

    else:
        result = Commdisaster.objects.values()
        return  render(request, "index.html",{'info':result})
    


def writeToDb(filepath):
    json_data=open(filepath,encoding='utf-8').read()
    data=json.loads(json_data,strict=False)
    for item in data:
        Commdisaster.objects.create(id=item.get('Code'),date=item.get('Date'),
        location=item.get('Location'),type=item.get('Type'),grade=item.get('Grade'),
        note=item.get('Note'),reportingunit=item.get('ReportingUnit'))


class CommdisasterViewSet(viewsets.ModelViewSet):
    queryset = Commdisaster.objects.all()
    serializer_class = CommdisasterSerializers
    
    # 返回时间顺序的所有数据。
    @action(methods=['get'],detail=False)
    def sort_by_time(self,request):
        commdisaster = Commdisaster.objects.order_by('date')[:] 
        # json data
        serializer = CommdisasterSerializers(instance=commdisaster,many=True)
        return Response(serializer.data)

    @action(methods=['get'],detail=False)
    def get_all_code(self,request):
        code = Commdisaster.objects.values('id')
        # serializer = CommdisasterSerializers(instance=code,many=True)
        # return Response(serializer.data)
        return Response(code)

    @action(methods=['post','get'],detail=False)
    def get_code_with_kd(self,request):
        pk=request.POST.get('pk')
        result = Commdisaster.objects.filter(id=pk)
        serializer = CommdisasterSerializers(instance=result,many=True)
        return Response(serializer.data)
    # def plaintext(self, request, *args, **kwargs):
    #     """自定义 Api 方法"""
    #     model = self.get_object()
    #     return Response(repr(model))

