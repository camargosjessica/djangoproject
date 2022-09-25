from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members


def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))


def welcome(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render({}, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    x = request.POST['user']
    y = request.POST['password']
    member = Members(user=x, password=y)
    member.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    user = request.POST['user']
    password = request.POST['password']
    member = Members.objects.get(id=id)
    member.user = user
    member.password = password
    member.save()
    return HttpResponseRedirect(reverse('index'))
