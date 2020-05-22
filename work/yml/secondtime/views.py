from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
import os,json
from django.core import serializers
from django.http import HttpResponse,FileResponse
from django.forms.models import model_to_dict

# Create your views here.
def home_page(request):
    result = Commdisaster.objects.values()
    return render(request,'secondindex.html',{'info':result})

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


def download_file(request):
    data=Commdisaster.objects.filter()
    data = serializers.serialize("json", data,ensure_ascii=False)
    print(type(data))
    response =FileResponse(data)
    response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
    response['Content-Disposition'] = 'attachment;filename="data.json"'
    return response

def upload_file(request):
    mscode = request.POST.get('mscode')
    if len(mscode)<1:
        return HttpResponse('mscode is error')
    # 请求方法为POST时，进行处理
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，则默认为None
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("没有需要上传的文件")
        else:
            absdir = os.path.dirname(os.path.abspath(__file__))
            try:
                with open(absdir+"/static/filestore/%s" % File.name, 'wb+') as f:
                    for chunk in  File.chunks():
                        f.write(chunk)
                # wri]te the info to db
                
                writeToDb(absdir+"/static/filestore/%s" % File.name)
                return HttpResponse("UPload over!")
            except FileNotFoundError as e:
                print(e)
                return HttpResponse("no error")

    else:
        result = Commdisaster.objects.values()
        return  render(request, "secondindex.html",{'info':result})

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

class CivilstructureViewSet(viewsets.ModelViewSet):
    queryset = Civilstructure.objects.all()
    serializer_class = CivilstructureSerializers
    # 返回时间顺序的所有数据。
    @action(methods=['get'],detail=False)
    def sort_by_time(self,request):
        civilstructure = Civilstructure.objects.order_by('date')[:] 
        # json data
        serializer = CivilstructureSerializers(instance=civilstructure,many=True)
        return Response(serializer.data)

    @action(methods=['get'],detail=False)
    def get_all_code(self,request):
        code = Civilstructure.objects.values('id')
        return Response(code)
    # 根据ID查询对应的信息
    @action(methods=['post','get'],detail=False)
    def get_code_with_id(self,request):
        pk=request.POST.get('pk')
        result = Civilstructure.objects.filter(id=pk)
        serializer = CivilstructureSerializers(instance=result,many=True)
        return Response(serializer.data)

class DeathstatisticsViewSet(viewsets.ModelViewSet):
    queryset = Deathstatistics.objects.all()
    serializer_class = DeathstatisticsSerializers
    # 根据ID查询对应的信息
    @action(methods=['post','get'],detail=False)
    def get_code_with_id(self,request):
        pk=request.POST.get('pk')
        result = Deathstatistics.objects.filter(id=pk)
        serializer = DeathstatisticsSerializers(instance=result,many=True)
        return Response(serializer.data)


class CollapserecordViewSet(viewsets.ModelViewSet):
    queryset = Collapserecord.objects.all()
    serializer_class = CollapserecordSerializers
    # 根据ID查询对应的信息
    @action(methods=['post','get'],detail=False)
    def get_code_with_id(self,request):
        pk=request.POST.get('pk')
        result = Collapserecord.objects.filter(id=pk)
        serializer = CollapserecordSerializers(instance=result,many=True)
        return Response(serializer.data)

class DisasterpredictionViewSet(viewsets.ModelViewSet):
    queryset = Disasterprediction.objects.all()
    serializer_class = DisasterpredictionSerializers

    # 根据ID查询对应的信息
    @action(methods=['post','get'],detail=False)
    def get_code_with_id(self,request):
        pk=request.POST.get('pk')
        result = Disasterprediction.objects.filter(id=pk)
        serializer = DisasterpredictionSerializers(instance=result,many=True)
        return Response(serializer.data)