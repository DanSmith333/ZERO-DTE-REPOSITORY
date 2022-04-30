from django.shortcuts import render

# Create your views here.
from .models import Parameters, Assumptions

def home(request):
    print('=================================================================== @' + request.method)


    if request.method == 'POST':
        print ('hello there underwear!')
        say_hi(request)

        # import function to run
        #from path_to_script import function_to_run

        # call function
        #function_to_run() 

        # return user to required page
        #return HttpResponseRedirect(reverse(app_name:view_name)


    return render(request, 'monte_carlo\home_X.html')

def say_hi(request):
    print ('Hello There Way Over There!')
    return render(request, 'monte_carlo\home_X.html')
