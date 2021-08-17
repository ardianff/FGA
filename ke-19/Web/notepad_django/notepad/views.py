from django.shortcuts import render, redirect

from .models import Notepad
from .forms import NotepadForm      

# Create your views here.                                                                    

def view(request, get_id):
    data = {} 
    data['notepad'] = Notepad.objects.get(get_id=get_id)    
    return render(request, 'notepad/view.html', data)

def create(request):  
    data = {} 
    form = NotepadForm(request.POST or None)
    if form.is_valid(): 
        form.save() 
        return redirect('url_list')
    data['form'] = form             
    return render(request, 'notepad/create.html', data)
def edit(request, get_id):  
    data = {}
    notepad = Notepad.objects.get(get_id=get_id)  
    form = NotepadForm(request.POST or None, instance=notepad)
    if form.is_valid():  
        form.save()
        return redirect('url_list')   
    data['form'] = form
    data['notepad'] = notepad
    return render(request, 'notepad/edit.html', data)

def remove(request, get_id): 
    notepad = Notepad.objects.get(get_id=get_id)
    notepad.delete()
    return redirect('url_list')
 
def list_data(request):                           
    data = {}
    data["list"] = Notepad.objects.all()
    return render(request, 'notepad/list.html', data)
