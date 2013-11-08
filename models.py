#!/usr/bin/python

class Page(models.Model):
  name = models.CharField(max_length=64)
  desc = models.CharField(max_length=64)
  
class Category(models.Model):
  types = models.IntegerField()  #读写等
  

class ownPermission(models.Model):
  page = models.ForeignKey(Page)
  perm = models.ForeignKey(Category)
  user = models.ForeignKey(User)
  
  
