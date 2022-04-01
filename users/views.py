# from multiprocessing import context

from django.contrib.auth import login as log_in
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import CustomUserCreationForm, UserForm

# Create your views here.

def login(request):
    """login view"""
    return render(request, 'login.html')

def logout(request):
    """logout view"""
    return render(request,'logout.html')

def account(request):
    """ view to see account details """
    form=UserForm()
    return render(request, "users/account.html", {"form":form})

def signup(request):
    """ view to sign up """
    if request.method == "GET":
        return render(
            request, "registration/signup.html",
            {"form": CustomUserCreationForm})

    form = CustomUserCreationForm(request.POST)

    if form.is_valid():
        user = form.save()
        log_in(request, user)
        return redirect(reverse("index"))

    username=request.POST['username']
    email=request.POST['email']
    password1=request.POST['password1']
    password2=request.POST['password2']
    context = {"message":"Tous les champs sont obligatoires.", "advice":"Vérifiez votre saisie.", "form":form}

    
    if User.objects.filter(username=username).exists():
        context["message"]="Le nom de l'utilisateur est déjà attribué."
        context["advice"]="Choisissez un autre nom d'utilisateur"
        return render(request, 'registration/signup.html', context)
        
    if User.objects.filter(email=email).exists():
        context["message"]="Cet e-mail est déjà attribué à un utilisateur existant."
        context["advice"]="Choisissez une autre adresse e-mail."
        return render(request, 'registration/signup.html', context)
        
    if password1 != password2:
        context["message"]="Les mots de passe ne correspondent pas."
    
    return render(request, 'registration/signup.html', context)
