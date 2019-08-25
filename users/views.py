from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, View
from .models import CustomUser

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserView(View):
    model = CustomUser

class UserUpdate(UpdateView, UserView):
    model = CustomUser
    fields = [
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'address',
        ]
    
    def get_success_url(self):
        return reverse_lazy('home')
