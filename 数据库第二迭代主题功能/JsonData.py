import pymysql
import json
# import Data
from Data import Data

class JsonData:
    #初始化数据项
    def __init__(self):

        self.filepath = ""
        self.MsCode = ""
        self.file = None

    #打开、json文件
    def loadJson(self):
        self.filepath = input("请输入json文件路径：\n")
        self.MsCode = input('请输入json数据源类型：\n')
        self.file = open(self.filepath, 'r', encoding='utf-8')

    # 读取json某一行
    def readJson(self, line):
        dic = json.loads(line)

        # 拿到json对应字段的值 类型全为  string
        data = Data()
        dic['ReportingUnit'] = self.MsCode + '_' + dic['ReportingUnit']
        data.setData(dic['Code'],dic['Date'],dic['Type'],dic['Grade'],dic['Picture'],dic['Note'],dic['ReportingUnit'],dic['Status'])
        return data

    def getFileConnecton(self):
        return self.file

    def disconn(self):
        self.file.close()



if __name__=='__main__':
    jsondata = JsonData()
    jsondata.loadJson()
    # 设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错

    # 读取每一行，读出 然后写入数据库
    for line in jsondata.getFileConnecton().readlines():
        result = jsondata.readJson(line)
        result.getLocationFromCode()

        #将读取到的数据插入到数据库中，注意多次插入会存在重复的问题，第二次执行需手动清空commdisaster表中的数据
        result.insertIntoCommDisaster()

        #数据保存,注意，如果重复多次
        jsondata.getFileConnecton()

        #将json文件导出到本地
        result.saveAsJson()
        #print(result.code)
    jsondata.disconn()
