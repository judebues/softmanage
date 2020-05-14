import pymysql
import json
import codecs
class Data:
    #建立连接，初始化数据
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='zmd526925',
                                          db='mshd',
                                          charset='UTF8',
                                          cursorclass=pymysql.cursors.DictCursor)

        self.code = ""
        self.location = ""
        self.date = ""
        self.type = ""
        self.grade = ""
        self.picture = ""
        self.reportingUnit = ""
        self.status = ""
        self.seqNum = ''
        self.disType = ''

    #修改类的属性值，用于记录读出来的数据
    def setData(self,code1,date1,type1,grade1,picture1,note1,reportingUnit1,status1):
        self.code = code1
        #self.location = location
        self.date = date1
        self.type = type1
        self.grade = grade1
        self.picture = picture1
        self.note = note1
        self.reportingUnit = reportingUnit1
        self.status = status1
        self.seqNum = code1[15:19]
        #self.disType =

    #与mysql建立连接
    def setMysqlConnection(self):
        self.connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='zmd526925',
                                 db='mshd',
                                 charset='UTF8',
                                 cursorclass=pymysql.cursors.DictCursor)
        return self.connection
    #取消连接
    def cutMysqlConnection(self):
        self.connection.close()

    #从 code 的19位编码中获取灾情发生的地址
    def getLocationFromCode(self):
       # self.code = "3311111111113360001"

        with self.connection.cursor() as cursor:
            sql = 'select info from mshd.province where code = %s'
            cursor.execute(sql, (self.code[0:2]))
            province = cursor.fetchone()
            province = province['info']

            sql = 'select info from mshd.city where code = %s'
            cursor.execute(sql, (self.code[2:4]))
            city = cursor.fetchone()
            city = city['info']

            sql = 'select info from mshd.county where code = %s'
            cursor.execute(sql, (self.code[4:6]))
            county = cursor.fetchone()
            county = county['info']

            sql = 'select info from mshd.street where code = %s'
            cursor.execute(sql, (self.code[6:9]))
            street = cursor.fetchone()
            street = street['info']

            sql = 'select info from mshd.community where code = %s'
            cursor.execute(sql, (self.code[9:12]))
            community = cursor.fetchone()
            community = community['info']

            self.location = province + city + county + street + community
        return self.location

    # 从code 的19位数字中 获取灾情类型
    def getDisType(self):
        #self.code = '3311111111113360001'

        with self.connection.cursor() as cursor:
            sql = 'select info from mshd.disInfo_mainClass where code = %s'
            cursor.execute(sql, (self.code[12]))
            disInfo_mainClass = cursor.fetchone()
            disInfo_mainClass = disInfo_mainClass['info']

            sql = 'select info from mshd.disInfo_subClass where code = %s'
            cursor.execute(sql, (self.code[13:15]))
            disInfo_subClass = cursor.fetchone()
            disInfo_subClass = disInfo_subClass['info']

            self.disType = disInfo_mainClass +'中的'+ disInfo_subClass
            print(self.disType)
        return self.disType

    #获得要存储的表的名字
    def getDisTableName(self):
        self.code = '3311111111113360001'

        with self.connection.cursor() as cursor:
            sql = 'select info from mshd.disInfo_tableName where code = %s'
            cursor.execute(sql, (self.code[12:15]))
            disInfo_tableName = cursor.fetchone()
            disInfo_tableName = disInfo_tableName['info']
        print(disInfo_tableName)


    #将数据 插入到本地mysql中
    def insertIntoCommDisaster(self):
        with self.connection.cursor() as cursor:
            sql = 'insert into mshd.CommDisaster(ID,date,location,type,grade,note,reportingUnit) value(%s,%s,%s,%s,%s,%s,%s)'
            ID = self.code
            date = self.date
            location = self.location
            type = self.type
            grade = self.grade
            note = self.note
            reportingUnit = self.reportingUnit

            cursor.execute(sql,(ID,date,location,type,grade,note,reportingUnit))

            # 检验插入结果是否正确，进行一次显示操作
            sql = "select * from mshd.CommDisaster;"
            cursor.execute(sql)

            # 获得结果并返回
            result = cursor.fetchone()
            print(result)
        self.connection.commit()

    #将当前data对象中记录的数据保存为对应类型的json文件，输出到本地
    def saveAsJson(self):

        code_dict = {'Code': self.code}
        date_dict = {'Date': self.date}
        location_dict = {'Location': self.location}
        type_dict = {'Type': self.type}
        grade_dict = {'Grade': self.grade}
        picture_dict = {'picture': self.picture}
        note_dict = {'Note': self.note}
        status_dict = {'Status': self.status}
        reportingUnit_dict = {'ReportingUnit': self.reportingUnit}

        jsonResult = code_dict,date_dict,location_dict,type_dict,grade_dict,picture_dict,note_dict,status_dict,reportingUnit_dict

        print(location_dict)
        filename = self.code[12:15] + '.json'
        with open(filename, 'w',encoding='unicode-escape') as file_obj:
            json.dump(jsonResult, file_obj)


# if __name__=='__main__':
#     data = Data()
#     data.setMysqlConnection()
#     data.getLocationFromCode()
#
#     data.getDisTableName()
#     # str =  "3311111111113360001"





