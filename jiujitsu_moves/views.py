from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Moves
from .forms import AddMoveForm

# Create your views here.


def index(request):
    return render(request, "moves/index.html")


def add_move(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddMoveForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            form.save() 
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/add-move?saved=true")
        
        else:
            
            return HttpResponseRedirect("/add-move?saved=false")
            
    else:
        form = AddMoveForm()
    
        return render(request, 'moves/addmove.html', {'form': form})
        
        
def search_moves(request): 
    
    move_list = Moves.objects.values()
    
    return render(request, 'moves/searchmove.html', {'move_list': move_list})
    
    
def half_guard_moves(request):

    half_guard_moves = Moves.objects.values('name').filter(position_id=1, is_offence=1)

    return render(request, "moves/halfguardmoves.html", {'half_guard_moves': half_guard_moves})

        