from django.shortcuts import render, HttpResponse
from datetime import datetime
from example.models import Contact
from django.contrib import messages

# Create your views here.
context = {
     "variable1": "Hello I am variable_1.\n",
     "variable2": "Hello I am variable_2.\n",
     "variable3": "Hello I am variable_3."
}

def index(request):
    return render(request, 'index.html', context)
    #return HttpResponse("This is Homepage.")


def about(request):
    return render(request, 'about.html', context)


def services(request):
    return render(request, 'services.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Thank You! Your response will be reverted back to you as soon as possible :)')
    return render(request, 'contact.html', context)


def Students(request):
    return render(request, 'Students.html', context)


def Faculty(request):
    return render(request, 'Faculty.html', context)


def Home(request):
    return render(request, 'index.html', context)
