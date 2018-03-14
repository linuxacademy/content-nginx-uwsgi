from django.urls import path

from . import views

urlpatterns = [
    path('', views.NoteIndex.as_view(), name='note_index'),
    path('new', views.NoteCreate.as_view(), name='new_note'),
    path('<int:note_id>/edit', views.NoteUpdate.as_view(), name='edit_note'),
    path('<int:note_id>/delete', views.NoteDelete.as_view(), name='delete_note'),
]
