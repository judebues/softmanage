from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
import os,json,datetime,pytz
from django.core import serializers
from django.http import HttpResponse,FileResponse
from django.forms.models import model_to_dict

# Create your views here.
def home_page(request):
    result = Commdisaster.objects.values()
    # writeToDB()
    # time < current_time
    # current_time = datetime.date.today()-
    # print(current_time)
    # print(datetime.datetime(2020,3,4,20, 8, 7, 127325))
    # result = Commdisaster.objects.filter(date__gt=datetime.date(2020,1,2))
    return render(request,'index2.html',{'info':result})
    

def delete_Comm(request,nid):
    Commdisaster.objects.filter(id=nid).delete()
    result=Commdisaster.objects.values()
    return render(request,'CommDisaster.html',{'info':result})
def delete_death(request,nid):
    Deathstatistics.objects.filter(id=nid).delete()
    result=Deathstatistics.objects.values()
    return render(request,'DeathStatistics.html',{'info':result})
def delete_civil(request,nid):
    Civilstructure.objects.filter(id=nid).delete()
    result=Civilstructure.objects.values()
    return render(request,'CivilStructure.html',{'info':result})

def send(request):
    return render(request,'send.html',)

def update_the_model(request):
    current_time = datetime.data.today()-datetime.timedelta(days=30)


def time_update_ready(time,className):
    value =  className.objects.filter()

def sendinfo(request):
    data=[]
    if request.method == "POST":
        list_death=request.POST.getlist('death_list')
        print(list_death)
        # if len(list_death)>1:
        #     writeToSend(data,list_death,'death_list')
        # struct_destory=request.POST.getlist('struct_destory')
        # if len(struct_destory)>1:
        #     writeToSend(data,struct_destory,'struct_destory')

        # LifelineEngineeringDisaster=request.POST.getlist('LifelineEngineeringDisaster')
        # if len(LifelineEngineeringDisaster)>1:
        #     writeToSend(data,LifelineEngineeringDisaster,'LifelineEngineeringDisaster')
        # secondarydisaster=request.POST.getlist('secondarydisaster')
        # if len(secondarydisaster)>1:
        #     writeToSend(data,secondarydisaster,'secondarydisaster')
        # Shock=request.POST.getlist('Shock')
        # if len(Shock)>1:
        #     writeToSend(data,Shock,'Shock')
        response =FileResponse(json.dumps(data))
        response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="data.json"'
        return HttpResponse("发送成功")


def writeToSend(list_value,listname):
    data={}
    if listname == "death_list":
        if '1' in list_value:
            data=dict(data,**model_to_dict(Commdisaster.objects.filter()))
        if '2' in list_value:
            data=dict(data,**model_to_dict(Commdisaster.objects.filter()))
    elif listname=="struct_destory":
        if '1' in list_value:
            data=dict(data,**model_to_dict(Commdisaster.objects.filter()))
        if '2' in list_value:
            data=dict(data,**model_to_dict(Commdisaster.objects.filter()))
    elif listname=="LifelineEngineeringDisaster":
        if '1' in list_value:
            data=dict(data,**model_to_dict(Commdisaster.objects.filter()))
        if '2' in list_value:
            data=dict(data,**model_to_dict(Commdisaster.objects.filter()))
    elif listname=="secondarydisaster":
        if '1' in list_value:
            data=dict(data,**model_to_dict(Commdisaster.objects.filter()))
        if '2' in list_value:
            data=dict(data,**model_to_dict(Commdisaster.objects.filter()))
    elif listname=="Shock":    
        if '1' in list_value:
            data=dict(data,**model_to_dict(Commdisaster.objects.filter()))
        if '2' in list_value:
            data=dict(data,**model_to_dict(Commdisaster.objects.filter()))
    return data

# search info according the request
# def search_info(request):
def search(request):
    results={}
    if request.method == "POST":
        search_code = request.POST.get('search')
        if len(search_code) != 19 and len(search_code)!=3: 
            return HttpResponse("数据格式输入错误，请重新输入")
        elif len(search_code) < 1:
            results = Commdisaster.objects.values()
        elif len(search_code) == 19:
            results = Commdisaster.objects.filter(id=search_code)
        elif len(search_code) == 3:
            if accordMscodeToTheClass(search_code)!=None:
                results = accordMscodeToTheClass(search_code).objects.values()
            else:
                return HttpResponse("error")
    if len(results)<1:
        return render(request,'searchresult.html',)
    return render(request,'datashow.html',{'info':results})

def accordMscodeToTheClass(mscode):
    if mscode == '441':
        return Collapserecord
    elif mscode == '336':
        return Commdisaster
    elif mscode == '221':
        return Civilstructure
    elif mscode == '111':
        return Deathstatistics
    elif mscode == '552':
        return Disasterprediction
    else:
        return None

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
    
    if len(mscode) < 1:
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
                theWrongWayToStoreDb(absdir+"/static/filestore/%s" % File.name,mscode)
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

def writeToDatabases(filepath,ClassName):
    json_data=open(filepath,encoding='utf-8').read()
    data=json.loads(json_data,strict=False)
    for item in data:
        temp = ClassName()
        allattr=temp.__dict__.keys()
        for i in range(len(allattr)):
            temp.allattr[i]=item.get(allattr[i])
        temp.save()
        
def theWrongWayToStoreDb(filepath,mscode):
    json_data=open(filepath,encoding='utf-8').read()
    data=json.loads(json_data,strict=False)
    if mscode == '441':
        for item in data:
            Collapserecord.objects.create(id=item.get('Code'),date=item.get('Date'),
        location=item.get('Location'),type=item.get('Type'),status=item.get('Status'),
        note=item.get('Note'),reportingunit=item.get('ReportingUnit'))
    elif mscode == '336':
        for item in data:
            Commdisaster.objects.create(id=item.get('Code'),date=item.get('Date'),
        location=item.get('Location'),type=item.get('Type'),grade=item.get('Grade'),
        note=item.get('Note'),reportingunit=item.get('ReportingUnit'))
    elif mscode == '221':
        for item in data:
            Civilstructure.objects.create(id=item.get('Code'),date=item.get('Date'),
        location=item.get('Location'),basicallyintactsquare=item.get('Basicallyintactsquare'),
        damagedsquare=item.get('Damagedsquare'),distoryedsquare=item.get('Distoryedsquare'),
        note=item.get('Note'),reportingunit=item.get('ReportingUnit'))
    elif mscode == '111':
        for item in data:
            Deathstatistics.objects.create(id=item.get('Code'),date=item.get('Date'),
        location=item.get('Location'),number=item.get('Number'),reportingunit=item.get('ReportingUnit'))
    elif mscode == '552':
        for item in data:
            Disasterprediction.objects.create(id=item.get('Code'),date=item.get('Date'),
        location=item.get('Location'),longitude=item.get('Longitude'),latitude=item.get('Latitude'),
        depth=item.get('Depth'),magnitude=item.get('Magnitude'),itensity=item.get('Itensity'),
        type=item.get('Type'),status=item.get('Status'),note=item.get('Note'),reportingunit=item.get('ReportingUnit'))




def commdisaster(request):
    result = Commdisaster.objects.values()
    return render(request,'CommDisaster.html',{'info':result})
def deathstatistics(request):
    result = Deathstatistics.objects.values()
    return render(request,'DeathStatistics.html',{'info':result})
def disasterprediction(request):
    result = Disasterprediction.objects.values()
    return render(request,'Disasterprediction.html',{'info':result})
def collapserecord(request):
    result = Collapserecord.objects.values()
    return render(request,'Collapserecord.html',{'info':result})
def civilstructure(request):
    result = Civilstructure.objects.values()
    return render(request,'CivilStructure.html',{'info':result})



# def writeToDB():
#     absdir = os.path.dirname(os.path.abspath(__file__))
#     filepath=absdir+"/static/filestore/data.json"
#     MsCode = "202"
#     file_name = open(filepath, 'r', encoding='utf-8')
#     for line in file_name.readlines():
#         dic = json.loads(line,strict=False)
#         #取值
#         dic['ReportingUnit'] = MsCode + '-' + dic['ReportingUnit']
#         code = dic['Code']
#         disasterType = code[12:15]
#         #print(disasterType)
#         #print(type(disasterType))
#         #根据类型编码判断要放入哪个表中
#         print(dic)
#         print("************")
#         if (disasterType == '336'):
#             # if Commdisaster.objects.filter(id=dic.get('Code'))==None:
#             Commdisaster.objects.create(id=dic.get('Code'),date=dic.get('Date'),location=dic.get('Location'),type=dic.get('Type'),grade=dic.get('Grade'),note=dic.get('Note'),reportingunit=dic.get('ReportingUnit'))
#         elif(disasterType == '111'):
#             # if Deathstatistics.objects.filter(id=dic.get('Code'))==None:
#             Deathstatistics.objects.create(id=dic.get('Code'),date=dic.get('Date'),location=dic.get('Location'),
#             number=dic.get('Number'),reportingunit=dic.get('ReportingUnit'))
#         elif(disasterType == '221'):
#             # if Civilstructure.objects.filter(id=dic.get('Code'))==None:
#             Civilstructure.objects.create(id=dic.get('Code'),date=dic.get('Date'),location=dic.get('Location'),
#             basicallyintactsquare=dic.get('BasicallyIntactSquare'),damagedsquare=dic.get('DamagedSquare'),
#             distoryedsquare=dic.get('DestoryedSquare'),note=dic.get('Note'),reportingunit=dic.get('ReportingUnit'))
#     file_name.close()









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
        