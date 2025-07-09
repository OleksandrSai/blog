from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..forms.signup import BootstrapUserCreationForm


def signup_view(request):
    if request.method == "POST":
        form = BootstrapUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("article-list")
    else:
        form = BootstrapUserCreationForm()  # <-- і тут теж твоя форма
    return render(request, "registration/signup.html", {"form": form})
