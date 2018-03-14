from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import edit, ListView
from django.contrib import messages

from .models import Note

class NoteIndex(LoginRequiredMixin, ListView):
    template_name = 'notepad/notes_index.html'
    context_object_name = 'notes'

    def get_queryset(self):
        """
        Return the notes for the user
        """
        return Note.objects.filter(user_id=self.request.user.id)

class NoteCreate(LoginRequiredMixin, edit.CreateView):
    """
    View for creating a new Note
    """
    model = Note
    fields = ['title', 'body']
    template_name = 'notepad/note_create.html'
    success_url = '/notes'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdate(LoginRequiredMixin, edit.UpdateView):
    """
    View for editing a Note
    """
    model = Note
    fields = ['title', 'body']
    pk_url_kwarg = 'note_id'
    template_name = 'notepad/note_update.html'
    success_url = '/notes'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user_id == request.user:
            messages.error(request, "You are not permitted to make that change.")
            return redirect('note_index')
        else:
            return super().dispatch(request, *args, **kwargs)

class NoteDelete(LoginRequiredMixin, edit.DeleteView):
    """
    View for deleting a Note
    """
    model = Note
    success_url = '/notes'
    pk_url_kwarg = 'note_id'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user_id == request.user:
            messages.error(request, "You are not permitted to make that change.")
            return redirect('note_index')
        else:
            return super().dispatch(request, *args, **kwargs)
