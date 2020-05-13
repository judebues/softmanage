# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def upload_file(request):
#     if request.method == "POST":
#         myFile = request.FILES.get("myfile",None)
#         if not myFile:
#             return HttpResponse("ERROR")
#         distion
from django.shortcuts import render
from django.http import HttpResponse
#import os
 
# Create your views here.
def upload_file(request):
    # 请求方法为POST时，进行处理
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，则默认为None
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("没有需要上传的文件")
        else:
            #打开特定的文件进行二进制的写操作
            #print(os.path.exists('/temp_file/'))
            with open("fileupload/filestore/%s" % File.name, 'wb+') as f:
                #分块写入文件
                for chunk in  File.chunks():
                    f.write(chunk)
            return HttpResponse("UPload over!")

    else:
        return  render(request, "fileupload.html")
