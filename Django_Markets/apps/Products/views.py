from __future__ import unicode_literals
from django.views.generic.base import TemplateView
## -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

## Using Django auth, login, and user classes
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
## Class based forms derived from models
from django.forms import ModelForm
## Using Django view Classes
from django.views import generic
## To view Django to SQL queries
from django.db import connection
# from django.contrib.auth.decorators import login_required
# from .forms import UserCreateForm, LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
#from ..Book_Reviews import urls
# home
from django.views.generic import FormView, TemplateView
#from articles.models import Article

## Simple view to capture keyword arguments
class HomePageView(TemplateView):
    print "Routed to Products: HomePageView"
    template_name = "Products/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super(HomePageView, self).get_context_data(**kwargs)
    #     context['latest_articles'] = Article.objects.all()[:5]
    #     return context

# def render_home(request):
#     print "routed to render_home"
#
#     return render(request, "Travel_Buddy/travels.html", context)
