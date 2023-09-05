from django.shortcuts import render
from django.http import HttpResponse
from .models import Person 


def index(request):

	return HttpResponse(Person.objects.all())
