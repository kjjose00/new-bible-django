# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bible(models.Model):
    id = models.IntegerField(primary_key=True)
    testament = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    bookname = models.TextField(blank=True, null=True)  # Field name made lowercase.
    bookno = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    chapter = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    verseno = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    verse = models.TextField(blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bible'
        db_table_comment = 'jjjj\t\t'
