from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    #Construct a dictionary to pass to the template engine as its context.
    #Note that the key boldmessage matches to {{ aboldmessage }} in the template
    context_dict = {"aboldmessage": "Crunchy, creamy, cookie, candy, cupcake!"}
    
    #Return a rendered response to the client. This can be done using the shortcut function 'render':
    return render(request, 'rango/index.html', context = context_dict)


def about(request):
    #fine to shorthand the context_dict like this if there isn't much to pass to it
    return render(request, 'rango/about.html', context = {"aboldmessage": "This tutorial has been put together by Rhys Stewart."} )