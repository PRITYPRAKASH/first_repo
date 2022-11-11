# Create views here._by prity

from msilib.schema import AdminExecuteSequence
import site
from django.http import HttpResponse,HttpResponseRedirect #views.py file return the request of httpresponse 
from django.shortcuts import render    #using templates we return the render The purpose of render() is to return an HttpResponse whose content is filled with the result of calling render_to_string() with the passed arguments.
from .models import Product

def index(request):
    return render(request,'david/index.html' )
def index(request):
    return render(request,'index.html' )

    # return HttpResponse("Home")

from django.template import loader
from .models import David
from django.urls import reverse
def index(request):
  mymembers = David.objects.all().values()
  output = ""
  for x in mymembers:
    output += x["firstname"]
  return HttpResponse(output)

def index(request):
  mymembers = David.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
       
def index(request):
  mymembers = David.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = David(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = David.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = David.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = David.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))