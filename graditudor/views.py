from pickletools import read_long1, read_unicodestring1
from django.shortcuts import render

# Create your views here.
from .models import Situation, Annoyance
import random


rand1 = 0
rand2 = 0


def home(request):
    # Get all Situations
    situations = Situation.objects.all()

    # Get all Annoyances
    annoyances = Annoyance.objects.all()

    # Render app template with context
    return render(request, 'graditudor/home.html', {'situations': situations, 'annoyances': annoyances})   
    

def random_graditude(request):

    global rand1
    global rand2

    
    # Get all Situations
    situations = Situation.objects.all()

    # Get all Annoyances
    annoyances = Annoyance.objects.all()
    
    rand1 = diff_random(0,len(situations)-1, rand1 )
    rand2 = diff_random(0,len(situations)-1, rand2 )

    random_situation = str(situations[rand1])
    random_annoyance = str(annoyances[rand2])


    print ('------------------------------------------------------------------------------', str(len(annoyances)))

    # Render app template with context
    return render(request, 'graditudor/one_graditudor.html', {'situation': random_situation, 'annoyance': random_annoyance})    



def diff_random (min, max, used ):
    while True:
        r = random.randint(min,max-1)
        if r != used:
            break

    return r

def new_function(request):
    # Get all Situations
    situations = Situation.objects.all()

    # Get all Annoyances
    annoyances = Annoyance.objects.all()


    random_index = random.randint(0,len(situations)-1)

    print ( 'Random situation: ' + str( situations[random_index])  ) 

    # Get all Annoyances
    annoyances = Annoyance.objects.all()

    # Render app template with context
    return render(request, 'graditudor/home.html', {'situations': situations[random_index], 'annoyances': annoyances})
