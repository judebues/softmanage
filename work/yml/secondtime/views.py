from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
import os,json,datetime,pytz,time
from django.core import serializers
from django.http import HttpResponse,FileResponse
from django.forms.models import model_to_dict

# Create your views here.
def home_page(request):
    result = Commdisaster.objects.values()
    return render(request,'index2.html',{'info':result})
    


# def update_the_model(request):
#     current_time = datetime.data.today()-datetime.timedelta(days=30)


# def time_update_ready(time,className):
#     value =  className.objects.filter()


def sendrecode(id,disastertype,o_url,reportingunit):
    date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    Disasterrequest.objects.create(id=id,date=date,disastertype=disastertype,status='0',o_url=o_url,reportingunit=reportingunit)

def updatesendrecode(request,id):
    Disasterrequest.objects.filter(id=id).update(status='1')
    result=Disasterrequest.objects.values()
    d1 = Disasterrequest.objects.filter(id=id)[0]
    disastertype = d1.id[12:15]
    date=time.strftime('%H:%M:%S',time.localtime(time.time()))
    path = '/home/data/'+disastertype+":"+date+".json"
    with open(path,'w+') as f:
        f.write(date)
    return render(request,'Disasterrequest.html',{'info':result})


def sendinfo(request):
    data=[]
    if request.method == "POST":
        if len(request.POST.get('URL')) < 1:
            return HttpResponse("发送失败,URL为空")    
        list_death=request.POST.getlist('info_list')
        # print(request.POST)
        # print(list_death)
        data=writeToSend(list_death)
        d1 = valueType(list_death).objects.all()[0]
        disastertype = d1.id[12:15]
        date=time.strftime('%H:%M:%S',time.localtime(time.time()))
        sendrecode(d1.id,disastertype,request.POST.get('URL'),d1.reportingunit)
        path = '/home/data/'+disastertype+":"+date+".json"
        with open(path,'w+') as f:
            f.write(date)
        # response =FileResponse(json.dumps(data))
        # response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
        # response['Content-Disposition'] = 'attachment;filename="data.json"'
        return HttpResponse("success")

def valueType(valuedd):
    list_object=[Deathstatistics,None,None,Civilstructure,None,None,None,None,None,None,None,None,None,Commdisaster,None,None,None,None,None,None,None,None,None,Disasterprediction]
    return list_object[int(valuedd[0])-1]

def writeToSend(value):
    if valueType(value)==None:
        return "null"
    data = valueType(value).objects.filter()
    data = serializers.serialize("json", data,ensure_ascii=False)
    return data

def download_file(request):
    data=Commdisaster.objects.filter()
    data = serializers.serialize("json", data,ensure_ascii=False)
    print(type(data))
    response =FileResponse(data)
    response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
    response['Content-Disposition'] = 'attachment;filename="data.json"'
    return response
# def search(request):
#     results={}
#     if request.method == "POST":
#         search_code = request.POST.get('search')
#         if len(search_code) != 19 and len(search_code)!=3: 
#             return HttpResponse("数据格式输入错误，请重新输入")
#         elif len(search_code) < 1:
#             results = Commdisaster.objects.values()
#         elif len(search_code) == 19:
#             results = Commdisaster.objects.filter(id=search_code)
#         elif len(search_code) == 3:
#             if accordMscodeToTheClass(search_code)!=None:
#                 results = accordMscodeToTheClass(search_code).objects.values()
#             else:
#                 return HttpResponse("error")
#     if len(results)<1:
#         return render(request,'searchresult.html',)
#     return render(request,'datashow.html',{'info':results})

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



def uploadfile(request):
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
                return HttpResponse("UPload over!")
            except FileNotFoundError as e:
                print(e)
                return HttpResponse("no error")
    # else:
        # result = Commdisaster.objects.values()
        # return  render(request, "secondindex.html",{'info':result})


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
def upload(request):
    return render(request,'UploadFile.html',)
def send(request):
    return render(request,'send.html',)
def sendlist(request):
    result = Disasterrequest.objects.values()
    return render(request,'Disasterrequest.html',{'info':result})
def sign_in(request):
    return render(request,'sign-in.html',{})
def sign_up(request):
    return render(request,'sign-up.html',{})

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
def delete_colla(request,nid):
    Collapserecord.objects.filter(id=nid).delete()
    result=Collapserecord.objects.values()
    return render(request,'Collapserecord.html',{'info':result})
def delete_request(request,nid):
    Disasterrequest.objects.filter(id=nid).delete()
    result=Disasterrequest.objects.values()
    return render(request,'Disasterrequest.html',{'info':result})









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
        



#         def writeToDb(filepath):
#     json_data=open(filepath,encoding='utf-8').read()
#     data=json.loads(json_data,strict=False)
#     for item in data:
#         Commdisaster.objects.create(id=item.get('Code'),date=item.get('Date'),
#         location=item.get('Location'),type=item.get('Type'),grade=item.get('Grade'),
#         note=item.get('Note'),reportingunit=item.get('ReportingUnit'))

# def writeToDatabases(filepath,ClassName):
#     json_data=open(filepath,encoding='utf-8').read()
#     data=json.loads(json_data,strict=False)
#     for item in data:
#         temp = ClassName()
#         allattr=temp.__dict__.keys()
#         for i in range(len(allattr)):
#             temp.allattr[i]=item.get(allattr[i])
#         temp.save()
        
# def theWrongWayToStoreDb(filepath,mscode):
#     json_data=open(filepath,encoding='utf-8').read()
#     data=json.loads(json_data,strict=False)
#     if mscode == '441':
#         for item in data:
#             Collapserecord.objects.create(id=item.get('Code'),date=item.get('Date'),
#         location=item.get('Location'),type=item.get('Type'),status=item.get('Status'),
#         note=item.get('Note'),reportingunit=item.get('ReportingUnit'))
#     elif mscode == '336':
#         for item in data:
#             Commdisaster.objects.create(id=item.get('Code'),date=item.get('Date'),
#         location=item.get('Location'),type=item.get('Type'),grade=item.get('Grade'),
#         note=item.get('Note'),reportingunit=item.get('ReportingUnit'))
#     elif mscode == '221':
#         for item in data:
#             Civilstructure.objects.create(id=item.get('Code'),date=item.get('Date'),
#         location=item.get('Location'),basicallyintactsquare=item.get('Basicallyintactsquare'),
#         damagedsquare=item.get('Damagedsquare'),distoryedsquare=item.get('Distoryedsquare'),
#         note=item.get('Note'),reportingunit=item.get('ReportingUnit'))
#     elif mscode == '111':
#         for item in data:
#             Deathstatistics.objects.create(id=item.get('Code'),date=item.get('Date'),
#         location=item.get('Location'),number=item.get('Number'),reportingunit=item.get('ReportingUnit'))
#     elif mscode == '552':
#         for item in data:
#             Disasterprediction.objects.create(id=item.get('Code'),date=item.get('Date'),
#         location=item.get('Location'),longitude=item.get('Longitude'),latitude=item.get('Latitude'),
#         depth=item.get('Depth'),magnitude=item.get('Magnitude'),itensity=item.get('Itensity'),
#         type=item.get('Type'),status=item.get('Status'),note=item.get('Note'),reportingunit=item.get('ReportingUnit'))