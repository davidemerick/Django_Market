# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import datetime

"""
Extend User to show understanding of Django
- maybe add something to Manager functionality
"""
#
# # Create your models here.
# # using User class
# # todo: extend User class to show understanding of django MTV
# class Trips(models.Model):
#     # for created by
#     # user = models.ForeignKey(User)
#     #related_name='users_who_joined'
#     # for those who join
#     #creator = models.CharField(max_length=128)
#     user = models.OneToOneField(User, related_name="creator")
#     travelers = models.ManyToManyField(User)
#     #travelers = models.ManyToManyField(User, through="Travelers")
#     destination = models.CharField(max_length=128)
#     description = models.TextField()
#     travel_start = models.DateTimeField()
#     travel_end = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add = True)
#     updated_at = models.DateTimeField(auto_now = True)
#
# # class Travelers(models.Model):
# #     trip = models.ForeignKey(Travels)
# #     user = models.ForeignKey(User)
#
#
#
#
# # ORM queries
# # .get(last_name='Thomas')
# # this returns the object matching a given condition
# # only works when object is unique
# # .filter(last_name='Thomas')
# # returns a QuerySet of objects matching query
# #
# # ? How to access QuerySet
# #
# # A manager is accessed via model classes, not per instance
# # User.objects is the Manager of object User
# # Each QuerySet is unique and not bound to the one in which it was created from.
# # QuerSets are stacked together and only executed when needed (the QuerySet is being evaluated)
