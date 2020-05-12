# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
