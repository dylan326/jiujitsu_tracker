from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import NameForm

# Create your views here.


def index(request):
    return render(request, "moves/index.html")


def addmove(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('add-move?move_added=true')
            
    else:
        form = NameForm()
        
    print(list(request.POST.items()))
    
    return render(request, 'moves/addmove.html', {'form': form})
        