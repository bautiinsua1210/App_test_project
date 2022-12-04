from django.shortcuts import render
from .models import Family
from django.http import HttpResponse





# Create your views here.


def family(request):
    relative = Family(name="Daniel", age="52")
    relative.save()
    text_string = f"Relative saved: Name:{relative.name}, Age:{relative.age}"
    return HttpResponse(text_string)