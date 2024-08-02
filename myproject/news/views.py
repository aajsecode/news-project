from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def home(request):
    all_news = models.News.objects.all()
    return render(
        request,
        "home.html",
        {"news_list": all_news, "number_of_news": all_news.__len__},
    )


def detail(request, pk):
    news = get_object_or_404(models.News, pk=pk)
    return render(request, "detail.html", {"news": news})
