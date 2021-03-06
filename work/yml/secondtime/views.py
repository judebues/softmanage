from django.shortcuts import render,redirect
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
import os,json,datetime,pytz,time
from django.core import serializers
from django.http import HttpResponse,FileResponse
from django.forms.models import model_to_dict
from .forms import *
import hashlib
from .timework import writeToDB

# Create your views here.
def home_page(request):
    result = Commdisaster.objects.values()
    dblist = ['Commdisaster','Deathstatistics','Collapserecord','Civilstructure','Disasterrequest']
    # print("*******************")
    # print("*******************")
    return render(request,'index2.html',{'options':dblist})
    


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
    return render(request,'DisasterRequest.html',{'info':result})


def sendinfo(request):
    data=[]
    if request.method == "POST":
        if len(request.POST.get('URL')) < 1:
            return HttpResponse("发送失败,URL为空")    
        list_death=request.POST.getlist('info_list')
        # print(request.POST)
        # print(list_death)
        data=writeToSend(list_death)
        if len(valueType(list_death).objects.all()) < 1:
            return HttpResponse("发送数据为空，停止发送")
        d1 = valueType(list_death).objects.all()[0]
        disastertype = d1.id[12:15]
        # date=time.strftime('%H:%M:%S',time.localtime(time.time()))
        sendrecode(d1.id,disastertype,request.POST.get('URL'),d1.reportingunit)
        # path = '/home/data/'+disastertype+":"+date+".json"
        # with open(path,'w+') as f:
        #     f.write(date)
        # response =FileResponse(json.dumps(data))
        # response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
        # response['Content-Disposition'] = 'attachment;filename="data.json"'
        return download_file()

def valueType(valuedd):
    list_object=[Deathstatistics,None,None,Civilstructure,None,None,None,None,None,None,None,None,None,Commdisaster,None,None,None,None,None,None,None,None,None,Disasterprediction]
    # print(valuedd[0])
    # print("***************")
    # print(str(list_object[0]))
    return list_object[int(valuedd[0])-1]

def writeToSend(value):
    if valueType(value)==None:
        return "null"
    data = valueType(value).objects.filter()
    data = serializers.serialize("json", data,ensure_ascii=False)
    return data

def download_file():
    data=Commdisaster.objects.filter()
    data = serializers.serialize("json", data,ensure_ascii=False)
    # print(type(data))
    response =FileResponse(data)
    response['Content-Type'] = 'application/octet-stream' #设置头信息，告诉浏览器这是个文件
    response['Content-Disposition'] = 'attachment;filename="data.json"'
    return FileResponse(response)

def search(request):
    results={}
    dblist = [Commdisaster,Deathstatistics,Collapserecord,Civilstructure,Disasterrequest]
    dbtemplate = ['CommDisaster.html','DeathStatistics.html','Collapserecord.html','CivilStructure.html','DisasterRequest.html']
    if request.method == "POST":
        search_code = request.POST.get('search')
        db_choose = int(request.POST.get('dbchoice'))-1

        if len(search_code) != 19: 
            return HttpResponse("数据格式输入错误，请重新输入")
        else:
            result=dblist[db_choose].objects.filter(id=search_code)
            return render(request,dbtemplate[db_choose],{'info':result})


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
    return render(request,'DisasterRequest.html',{'info':result})
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
    return render(request,'DisasterRequest.html',{'info':result})

def getDbAccordingId(nid):
    dblist=[Commdisaster,Deathstatistics,Civilstructure]
    infolist=['336','111','221']
    return dblist[infolist.index(nid[12:15])]

def update(request,nid):
    # result=[]
    # disasterType = nid[12:15]
    # if (disasterType == '336'):
    #     result = Commdisaster.objects.filter(id=dic.get('Code'))
    # elif(disasterType == '111'):
    #     Deathstatistics.objects.filter(id=dic.get('Code'))
    # elif(disasterType == '221'):
    #     Civilstructure.objects.filter(id=dic.get('Code'))

    result = getDbAccordingId(nid).objects.filter(id=nid)[0]
    # print(result.__dict__.keys())
    # print(result[0])
    di = model_to_dict(result)
    return render(request,'update_death.html',{'info':di})

def updateInfo(request):
    if request.method == "POST":
        value = dict(request.POST.dict())
        value.pop('csrfmiddlewaretoken')
        db = getDbAccordingId(value.get('id'))
        db.objects.filter(id=value.get('id')).delete()
        db.objects.create(**value)
    return redirect("/secondtime/index/")





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
        
def login(request):
    if request.session.get('is_login', None):
        return redirect("/secondtime/index/")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if user.password == password:  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/secondtime/login/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/secondtime/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户
                User.objects.create(username=username, password=password1, email=email)
                # return HttpResponse("%s,%s,%s,%s,%s"%(username,password1,email))
                return redirect('/secondtime/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/secondtime/login/')
    request.session.flush()

    return redirect('/secondtime/login/')


def hash_code(s, salt='mysite_login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()