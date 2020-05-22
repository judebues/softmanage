from django.db import models

# Create your models here.
# class Community(models.Model):
#     code = models.CharField(db_column='Code', primary_key=True, max_length=3)  # Field name made lowercase.
#     info = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'community'

# class County(models.Model):
#     code = models.CharField(db_column='Code', primary_key=True, max_length=2)  # Field name made lowercase.
#     info = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'county'

# class Province(models.Model):
#     code = models.CharField(db_column='Code', primary_key=True, max_length=2)  # Field name made lowercase.
#     info = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'province'

# class City(models.Model):
#     code = models.CharField(db_column='Code', primary_key=True, max_length=2)  # Field name made lowercase.
#     info = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'city'


# class Street(models.Model):
#     code = models.CharField(db_column='Code', primary_key=True, max_length=3)  # Field name made lowercase.
#     info = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'street'

# 次生灾害
class Collapserecord(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=19)  # Field name made lowercase.
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=3)
    status = models.CharField(max_length=3)
    note = models.CharField(max_length=200, blank=True, null=True)
    reportingunit = models.CharField(db_column='reportingUnit', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CollapseRecord'
        unique_together = (('id', 'date'),)

# 通信系统灾情统计表
class Commdisaster(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=19)  # Field name made lowercase.
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=2)
    grade = models.CharField(max_length=3)
    note = models.CharField(max_length=200, blank=True, null=True)
    reportingunit = models.CharField(db_column='reportingUnit', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commdisaster'
        unique_together = (('id', 'date'),)

# 土木结构房屋破坏统计表
class Civilstructure(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=19)  # Field name made lowercase.
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    basicallyintactsquare = models.CharField(db_column='basicallyIntactSquare', max_length=6)  # Field name made lowercase.
    damagedsquare = models.CharField(db_column='damagedSquare', max_length=6)  # Field name made lowercase.
    distoryedsquare = models.CharField(db_column='distoryedSquare', max_length=6)  # Field name made lowercase.
    note = models.CharField(max_length=200, blank=True, null=True)
    reportingunit = models.CharField(db_column='reportingUnit', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CivilStructure'
        unique_together = (('id', 'date'),)

# 111
# 人员伤亡及失踪数据库设计表
class Deathstatistics(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=19)  # Field name made lowercase.
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    number = models.CharField(max_length=5)
    reportingunit = models.CharField(db_column='reportingUnit', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DeathStatistics'
        unique_together = (('id', 'date'),)
        
# 灾情预测
class Disasterprediction(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=19)  # Field name made lowercase.
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    depth = models.FloatField()
    magnitude = models.FloatField()
    intensity = models.CharField(max_length=6)
    type = models.CharField(max_length=3)
    status = models.CharField(max_length=3)
    note = models.CharField(max_length=200, blank=True, null=True)
    reportingunit = models.CharField(db_column='reportingUnit', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DisasterPrediction'
        unique_together = (('id', 'date'),)


# 向请求方输出在清数据信息表
class Disasterrequest(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=19)  # Field name made lowercase.
    date = models.DateTimeField()
    disastertype = models.CharField(max_length=3)
    status = models.CharField(max_length=1)
    o_url = models.CharField(db_column='o_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    reportingunit = models.CharField(db_column='reportingUnit', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DisasterRequest'
        unique_together = (('id', 'date'),)