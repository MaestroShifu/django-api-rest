from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

class HelloWorld(View):
    def get(self, request):
        context = {
            'name': 'Daniel Steven Sarmiento',
            'age': 23,
            'codes': ['Python', 'Django', 'React']
        }
        return render(request, 'hello_world.html', context=context)
