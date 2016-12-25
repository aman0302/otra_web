from django.shortcuts import render
from .forms import RequestForm, RegisterForm
from .models import Register, Request

# Create your views here.
def index(request):
    return render(request,'index.html')

def requestQuote(request):
    print('requesting 1')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RequestForm(request.POST)
        # check whether it's valid:
        print (form)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return render(request,'done.html')

            # if a GET (or any other method) we'll create a blank form
    else:
        form = RequestForm()
        print(form)
        return render(request,'requestQuote.html',{'form':form})

def registerDriver(request):
    print('requesting 1')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        print (form)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return render(request,'done.html')

            # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()
        print(form)
        return render(request,'registerDriver.html',{'form':form})
