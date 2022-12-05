from django.shortcuts import render
from .models import Family
from django.http import HttpResponse
from django.template import Template, loader






# Create your views here.


"""def family(request):
    relative = Family(name="Lando", surname="Norris", age="23", born_year="1999")
    relative.save()
    text_string = f"Relative saved: Name:{relative.name}, Surname:{relative.surname}, Age:{relative.age} and Born Year:{relative.born_year}"
    return HttpResponse(text_string)   {"Relatives:" : relative}"""


"""def family(request):
    relative = Family(name="Lando", surname="Norris", age="23", born_date="1999-12-10")
    relative.save()
    relative = relative.objects.all()
    return render(request, "templates.html", f"Name: {relative.name}")"""

"""def family(request):
    relative = Family(name="Lando", surname="Norris", age="23", born_date="1999-12-10")
    relative.save()
    return render(request, "templates.html", f"Name: {relative.name}")"""

def family(request):
    relative1 = {"name":"Lando", "surname":"Norris", "age":"23", "born_date":"1999-12-10"}
    relative2 = {"name":"Mattia", "surname":"Binotto", "age":"53", "born_date":"1996-11-03"}
    relative3 = {"name":"Daniel", "surname":"Ricciardo", "age":"33", "born_date":"1989-07-01"}
    template = loader.get_template("templates.html")
    family1 = template.render(relative1)    
    return HttpResponse(family1)
