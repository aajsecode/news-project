from django.urls import path
from .views import home, detail

urlpatterns = [
    path("", home, name="home"),
    path("news/<int:pk>/", detail, name="detail"),
]
