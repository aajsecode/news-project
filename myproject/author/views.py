from django.shortcuts import render, redirect
from accounts.models import CustomUser
from news.models import News
from .forms import NewsCreateForm


# Create your views here.
def author_profile(request, pk):
    author = CustomUser.objects.get(pk=pk)
    author_posts = News.objects.filter(authored_by=author)

    return render(
        request, "profile.html", {"author": author, "author_posts": author_posts}
    )


def news_create(request):
    if request.POST:
        form = NewsCreateForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.authored_by = request.user
            news.save()

            return redirect("detail", pk=news.id)
    else:
        form = NewsCreateForm()
        return render(request, "create.html", {"form": form})


def news_update(request, pk):
    news = News.objects.get(pk=pk)
    if news.authored_by == request.user:
        if request.POST:
            form = NewsCreateForm(request.POST, request.FILES, instance=news)
            if form.is_valid():
                form.save()
                return redirect("detail", pk=news.id)
        else:
            form = NewsCreateForm(instance=news)
            return render(request, "update.html", {"form": form})
    else:
        return None


def news_delete(request, pk):
    news = News.objects.get(pk=pk)
    if news.authored_by == request.user:
        news.delete()
        return render(request, "delete.html", {"id": request.user.id})
    else:
        return None
