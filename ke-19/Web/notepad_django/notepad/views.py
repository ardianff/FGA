from django.shortcuts import render, redirect

from .models import Notepad
from .forms import NotepadForm      

# Create your views here.                                                                    

def view(request, pk):
    data = {} 
    data['notepad'] = Notepad.objects.get(pk=pk)    
    return render(request, 'notepad/view.html', data)

def create(request):  
    data = {} 
    form = NotepadForm(request.POST or None)
    if form.is_valid(): 
        form.save() 
        return redirect('url_list')
    data['form'] = form             
    return render(request, 'notepad/create.html', data)
def edit(request, pk):  
    data = {}
    notepad = Notepad.objects.get(pk=pk)  
    form = NotepadForm(request.POST or None, instance=notepad)
    if form.is_valid():  
        form.save()
        return redirect('url_list')   
    data['form'] = form
    data['notepad'] = notepad
    return render(request, 'notepad/edit.html', data)

def remove(request, pk): 
    notepad = Notepad.objects.get(pk=pk)
    notepad.delete()
    return redirect('url_list')
 
def list_data(request):                           
    data = {}
    data["list"] = Notepad.objects.all()
    return render(request, 'notepad/list.html', data)
