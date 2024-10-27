from django.views.generic import CreateView
from django.urls import reverse_lazy
from socialmedia.accounts.forms import UserCreationForm

class SignUpView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
