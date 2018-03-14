from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

class UserCreate(FormView):
    form_class = UserCreationForm
    template_name = 'signup/signup.html'
    success_url = '/notes'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)
