from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'testapp/index.html')

def result(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        qual = request.POST.get('qual')
        return render(request, 'testapp/result.html', {'name': name, 'age': age, 'qual': qual})
    return HttpResponse("Invalid request")

