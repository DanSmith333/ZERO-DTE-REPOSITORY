from django.shortcuts import render

# Create your views here.
from .models import Oscarrr



def home(request):
    print('home')
    return render(request, 'oscarrr\home.html')   

def doit(request):
    print('----------------------------------------------- doit')
    foo = 'bar'
    return render(request, 'oscarrr\doit.html', {'password':foo})


def user_parameters(request):
    parameters =  Oscarrr.objects.all()
    return render ( request, 'oscarrr/user_parameters.html', {'parameters':parameters})
