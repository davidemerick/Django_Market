## -*- coding: utf-8 -*-
from __future__ import unicode_literals
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
from .forms import UserCreateForm, LoginForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout
#from ..Book_Reviews import urls
# home
from django.views.generic import FormView, TemplateView

"""
TODO for Login_Reg: views.py
- index logic for incorrect login
:: index.html edited to reflect error
"""

## Rendering views ##
# class ContactView(FormView)

"""
View function for login/reg page
- Sends login and registration forms to index.html
"""
def index(request):
    print "routed to index"
    #print authUser
    registerFormToRender = UserCreateForm()
    # Using Django AuthForm vs extended LoginForm defined in forms.py
    loginFormToRender = AuthenticationForm()
    context={
        "registerForm":registerFormToRender,"loginForm":loginFormToRender, #"forErrors":authUser
    }

    # testing to show Django ORM/SQL queries
    showSQL = connection.queries
    print showSQL

    # connection.queries = []
    # Protocols.objects.filter(active=False)
    # print connection.queries
    return render(request, "Login_Reg/index.html", context)

"""
View function for 'login success'
"""
def renderSuccessfulLogin(request):
    print "routed to renderHome"
    #print connection.queries

    allUsers = User.objects.all()

    context= {
        "allUsers":allUsers
    }
    #
    for users in allUsers:
        print users.id

    return render(request, 'login-reg:render_index', context)

## Classes ##

"""
Generic class-based view for a list of Users, included for debugging purposes
"""
class UserListView(generic.ListView):
    model = User
    paginate_by = 5
    # template_name = 'dmke-Django/home.html'

## Functions, redirecting
def register(request):
    print "routed to register"
    newUser = UserCreateForm(request.POST)
    if newUser.is_valid():
        user = newUser.save(commit=False)
        user.save()
        print "Valid"
        return redirect(reverse('products-app:home'))
    else:
        request.session['register_errors'] = newUser
        print "Not valid"
        return redirect(reverse('login-reg:render_index'))
        #return HttpResponseRedirect(reverse('login-reg:render_index', args=(newUser)))
        #return render_to_response('/index.html', {'form': newUser})

def login(request):
    print "routed to login"
    authUser=authenticate(username=request.POST['username'], password=request.POST['password'])
    if authUser:
        print "User authenticated"
        auth_login(request, authUser)
    else:
        print "Unauth"
        return redirect('/')

    return redirect(reverse('products-app:home'))

def process_logout(request):
    print "routed to process_logout"
    logout(request)
    return redirect(reverse('login-reg:render_index'))


#@login_required(login_url='/')
# def login_success(request):
#     return render(request,"ourApp/show.html")

# class UserProfileView(DetailView):
#     model = User
#     slug_field = "username"
#     template_name = "userprofile.html"
#
# # accounts/urls.py
# from views import UserProfileView
# urlpatterns = patterns('',
#     # By user ID
#     url(r'^profile/id/(?P<pk>\d+)/$', UserProfileView.as_view()),
#     # By username
#     url(r'^profile/username/(?P<slug>[\w.@+-]+)/$', UserProfileView.as_view()),
# )


# from django.conf.urls import url
# from . import views
## This url pattern will route to views file and 'show' method
# urlpatterns = [
#     url(r'^/en/(?P<id>\d+)$', views.show)
# ]

# def show(request, id):
#   context = {
#     "id" : id
#   }
#   return render(request, "second_app/show.html", context)

  # <!-- Inside apps/first_app/templates/first_app/index.html -->
  # {% load staticfiles %}
  # <link rel="stylesheet" href="{% static 'first_app/css/styles.css' %}">
  # <script src="{% static 'first_app/js/main.js' %}" > </script>

  ## A variable in the class of a Django model is a column in the table (SQL DB)
  ## An instance/object of [class, model] is a row in the table

    # class Course(models.Model):
    #  name = models.CharField(max_length=255)
    #  description = models.TextField()
    #  created_at = models.DateTimeField(auto_now_add=True)
    #  updated_at = models.DateTimeField(auto_now=True)
  # foreign key in a class signifies a many to one relationship with class related to fk

  # courses = Course.objects.all()
  # for course in courses:
  #     print course.name, course.description

  # Django builds database as: appname + _ + lowercase_model_name

  # Entry.objects.filter(blog__name='Beatles Blog')
  # retrieves all Entry objects with a Blog whose name is 'Beatles Blog'
  #
  # Blog.objects.filter(entry__headline__contains='Lennon')
  # reverse relationship, retrieves all Blog objects which have at least one Entry object of headline "Lennon"
  # Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)
  # ^contains Lennon and also pub date 2008
  #
  # .filter, .filter = would select Lennon and then
  # double filter method is acting on blog QuerySet
  # F expressions:
  # Entry.objects.filter(authors__name=F('blog__name'))
  # all Entry objects where authors name is same as blog name
  #
  # from datetime import timedelta
  # Entry.objects.filter(mod_date__gt=F('pub_date') + timedelta(days=3))
  # Returns all entries modified more than 3 days after they were published
# Blog.objects.get(id__exact=14) # Explicit form
# Blog.objects.get(id=14) # __exact is implied
# Blog.objects.get(pk=14) # pk implies id__exact

# >>> Entry.objects.filter(blog__id__exact=3) # Explicit form
# >>> Entry.objects.filter(blog__id=3)        # __exact is implied
# >>> Entry.objects.filter(blog__pk=3)        # __pk implies __id__exact
# Entry.objects.filter(headline__contains='%')
#
# Poll.objects.get(
#     Q(question__startswith='Who'),
#     Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
# )
# Can delete QuerySets with .delete()
#
# this_book.publishers.add(this_publisher) is the same as this_publisher.books.add(this_book), and this_book.publishers.all() will return all publishers of a given book.

# #this_author = Author.objects.get(id=2)
# books = Book.objects.filter(author=this_author)
# # one-line version:
# books = Book.objects.filter(author=Author.objects.get(id=2))
