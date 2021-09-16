# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cookies(models.Model):
    value = models.CharField(max_length=20)
    newsid = models.IntegerField(db_column='newsId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cookies'


class Komentari(models.Model):
    author = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    news = models.IntegerField()
    likes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'komentari'


class Korisnici(models.Model):
    email = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=100)
    tip = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'korisnici'


class Lajkovi(models.Model):
    value = models.CharField(max_length=20)
    commentid = models.IntegerField(db_column='commentId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lajkovi'


class Vesti(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    count = models.IntegerField()
    category = models.CharField(max_length=20)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vesti'
