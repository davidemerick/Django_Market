# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductsManager(models.Manager):
    pass

# Create your models here.
# using User class
# todo: extend User class to show understanding of django MTV
class Products(models.Model):
    """
    #Relations
    #Attributes
    #Manager
    #Functions/methods
    #Meta

    """
    ## Relations
    #creator = models.ForeignKey(User, related_name="user_who_made")
    #travelers = models.ManyToManyField(User, related_name="users_who_joined")

    ## Attributes
    manufacturer = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    price = models.CharField(max_length=128)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    ## Manager
    objects = ProductsManager()
