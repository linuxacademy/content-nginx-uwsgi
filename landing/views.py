from django.shortcuts import render, redirect

from notepad.models import Note

def index(request):
    if request.user.is_authenticated:
        return redirect('note_index')
    else:
        try:
            note = Note.objects.latest()
        except:
            return render(request, 'landing/index.html', {})
        else:
            return render(request, 'landing/index.html', {'note': note})
