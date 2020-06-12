# 1:定期将数据写入数据库
import os,json
from os import listdir
from .models import *
def getAllFileFromDir():
    absdir = os.path.dirname(os.path.abspath(__file__))
    filepath=absdir+"/static/filestore/"    
    filename=listdir(filepath)
    return filename

def writeToDB(filename):
    absdir = os.path.dirname(os.path.abspath(__file__))
    filepath=absdir+"/static/filestore/"+filename
    MsCode = "202"
    try:
        file_name = open(filepath, 'r', encoding='utf-8')
        for line in file_name.readlines():
            dic = json.loads(line,strict=False)
            dic['ReportingUnit'] = MsCode + '-' + dic['ReportingUnit']
            code = dic['Code']

            province = Province.objects.filter(code=code[0:2])[0]
            
            city = City.objects.filter(code=code[2:4])[0]
            country = County.objects.filter(code=code[4:6])[0]
            street = Street.objects.filter(code=code[6:9])[0]
            community = Community.objects.filter(code=code[9:12])[0]
            print(province)
            print(type(province))
            print("*************")
            print(city)
            print(type(city))
            dic['Location'] = province.info + city.info + country.info + street.info + community.info
            
            disasterType = code[12:15]
            if (disasterType == '336'):
                Commdisaster.objects.filter(id=dic.get('Code')).delete()
                Commdisaster.objects.create(id=dic.get('Code'),date=dic.get('Date'),location=dic.get('Location'),type=dic.get('Type'),grade=dic.get('Grade'),note=dic.get('Note'),reportingunit=dic.get('ReportingUnit'))
            elif(disasterType == '111'):
                Deathstatistics.objects.filter(id=dic.get('Code')).delete()
                Deathstatistics.objects.create(id=dic.get('Code'),date=dic.get('Date'),location=dic.get('Location'),number=dic.get('Number'),reportingunit=dic.get('ReportingUnit'))
            elif(disasterType == '221'):
                Civilstructure.objects.filter(id=dic.get('Code')).delete()
                Civilstructure.objects.create(id=dic.get('Code'),date=dic.get('Date'),location=dic.get('Location'),basicallyintactsquare=dic.get('BasicallyIntactSquare'),damagedsquare=dic.get('DamagedSquare'),destoryedsquare=dic.get('DestoryedSquare'),note=dic.get('Note'),reportingunit=dic.get('ReportingUnit'))
        file_name.close()
    except Exception as e:
        print(e)
    
def timeWorkWriteFileToDb():
    print("write something to db")
    allfile =getAllFileFromDir()
    if allfile == None:
        return None
    for file in allfile:
        writeToDB(file)
    