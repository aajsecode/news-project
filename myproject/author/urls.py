from django.urls import path
from .views import author_profile, news_create, news_update, news_delete

urlpatterns = [
    path("profile/<int:pk>/", author_profile, name="author_profile"),
    path("create-post/", news_create, name="news_create"),
    path("update-post/<int:pk>/", news_update, name="news_update"),
    path("delete-post/<int:pk>/", news_delete, name="news_delete"),
]
