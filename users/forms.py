from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.urls import reverse_lazy


class CustomUserCreationForm(UserCreationForm):
    """ Custom form for signing up """
    class Meta(UserCreationForm.Meta):
        """ adding email field to default form """
        fields = UserCreationForm.Meta.fields + ("email",)
        success_url = reverse_lazy('login')
        template_name= 'registration/signup.html'

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
