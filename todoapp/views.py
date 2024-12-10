from django.shortcuts import render
from .models import Person
from django.http import HttpResponseRedirect

def home(request):
  user = Person.objects.all()
  return render(request, 'index.html',{'user': user})

def create (request):
  if request.method == 'POST':
    users = Person()
    users.name = request.POST.get('name')
    users.age = request.POST.get('age')
    users.save()
  return HttpResponseRedirect('/')

def delete(request,id):
  try:
    user=Person.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect('/')
  except Person.DoesNotExist:
    return HttpResponseRedirect('<h2>колдонуучу табылган жок</2>') 