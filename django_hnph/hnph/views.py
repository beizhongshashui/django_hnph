from django.shortcuts import render

# Create your views here.
def about(request):

    return render(request,'hnph/about.html')

def index(request):

    return render(request,'hnph/index.html')

def contact(request):

    return  render(request,'hnph/contact.html')

def services(request):

    return render(request,'hnph/services.html')