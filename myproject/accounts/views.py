from django.shortcuts import render, redirect
from .forms import AuthorSignup
from django.contrib.auth import login


# Create your views here.
def signup(request):
    if request.POST:
        form = AuthorSignup(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request=request, user=user)
            return redirect("home")
        else:

            return render(request, "signup.html", {"form": form})
    else:
        form = AuthorSignup()
        return render(request, "signup.html", {"form": form})
