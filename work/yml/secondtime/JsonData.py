import pymysql
import json
# import CommDisaster
from CommDisaster import CommDisaster
from DeathStatistics import DeathStatistics
from CivilStructure import CivilStructure
class JsonData:
    #初始化数据项
    def __init__(self):

        self.filepath = ""
        self.MsCode = ""
        self.file = None
    #打开、json文件
    def openJsonFile(self):
        self.filepath = input("请输入json文件路径：\n")
        self.MsCode = input('请输入json数据源类型：\n')
        self.file = open(self.filepath, 'r', encoding='utf-8')

    #处理commDisaster表的函数
    def commDisasterHandler(self,dic):
        # 赋值
        commdis = CommDisaster()
        dic['ReportingUnit'] = self.MsCode + '-' + dic['ReportingUnit']
        commdis.setCommDisaster(dic['Code'], dic['Date'], dic['Type'], dic['Grade'], dic['Picture'], dic['Note'],dic['ReportingUnit'], dic['Status'])
        #从ID字段解析location
        commdis.getLocationFromCode()
        # 将读取到的数据插入到数据库中，注意多次插入会存在重复的问题，第二次执行需手动清空commdisaster表中的数据
        commdis.insertIntoCommDisaster()
        #测试增删查改的调用数据
        # commdis.deleteCommDisaster('3311111111113360005')
        # commdis.insertCommDisaster('3311111111113360005', '2020-02-01 00:00:00', '1', 'I', 'I', '1', '1')
        # commdis.selectCommDisaster('3311111111113360005')
        # commdis.updateCommDisaster('3311111111113360005', 'ReportingUnit', '2')
        # 将json文件导出到本地
        commdis.saveAsJson()
        #中断其与mysql连接
        commdis.cutMysqlConnection()

        return commdis

    #处理deathstatistics 表的函数
    def deathStatisticsHandler(self,dic):
        #赋值
        deathsSta = DeathStatistics()
        dic['ReportingUnit'] = self.MsCode + '-' + dic['ReportingUnit']
        deathsSta.setDeathStatistics(dic['Code'], dic['Date'], dic['Number'], dic['ReportingUnit'])
        # 从ID字段解析location
        deathsSta.getLocationFromCode()
        # 将读取到的数据插入到数据库中，注意多次插入会存在重复的问题，第二次执行需手动清空commdisaster表中的数据
        deathsSta.insertIntoDeathStatistics()

        #测试增删查改的数据
        # deathsSta.deleteDeathStatistics('3311111111111110005')
        # deathsSta.insertDeathStatistics('3311111111111110005', '2020-02-01 00:00:00', '1', 'I','I')
        # deathsSta.selectDeathStatistics('3311111111111110005')
        # deathsSta.updateDeathStatistics('3311111111111110005', 'ReportingUnit', '2')

        # 将json文件导出到本地
        deathsSta.saveAsJson()
        # 中断其与mysql连接
        deathsSta.cutMysqlConnection()

        return deathsSta

    #处理civilStructure表的函数
    def civilStructureHandler(self,dic):
        # 赋值
        civilstr = CivilStructure()
        dic['ReportingUnit'] = self.MsCode + '-' + dic['ReportingUnit']
        civilstr.setCivilStructure(dic['Code'], dic['Date'], dic['BasicallyIntactSquare'], dic['DamagedSquare'], dic['DestoryedSquare'], dic['Note'],dic['ReportingUnit'])

        #从ID字段解析location
        civilstr.getLocationFromCode()
        # 将读取到的数据插入到数据库中，注意多次插入会存在重复的问题，第二次执行需手动清空commdisaster表中的数据
        civilstr.insertIntoCivilStructure()
        #测试增删查改的调用数据
        # civilstr.deleteCivilStructure('3311111111112210005')
        # civilstr.insertCivilStructure('3311111111112210005', '2020-02-01 00:00:00', '1', 'I','1','1','1','1')
        # civilstr.selectCivilStructure('3311111111112210005')
        # civilstr.updateCivilStructure('3311111111112210005', 'ReportingUnit', '2')

        # 将json文件导出到本地
        civilstr.saveAsJson()
        #中断其与mysql连接
        civilstr.cutMysqlConnection()

        return civilstr

    # 读取json某一行（一行为一条数据记录，可能要划分到不同的表）
    def readJsonALine(self, line):
        #读一行，将数据存到数据字典中，方便取值
        dic = json.loads(line)
        #取值
        code = dic['Code']
        disasterType = code[12:15]
        #print(disasterType)
        #print(type(disasterType))
        #根据类型编码判断要放入哪个表中
        if (disasterType == '336'):
            self.commDisasterHandler(dic)
        elif(disasterType == '111'):
            self.deathStatisticsHandler(dic)
        elif(disasterType == '221'):
            self.civilStructureHandler(dic)

    def getFileConnecton(self):
        return self.file

    def disconn(self):
        self.file.close()



if __name__=='__main__':
    jsondata = JsonData()
    jsondata.openJsonFile()
    # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错

    # 读取每一行，读出 然后写入数据库
    for line in jsondata.getFileConnecton().readlines():
        jsondata.readJsonALine(line)

    jsondata.disconn()
