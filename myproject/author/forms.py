from news.models import News
from django.forms import ModelForm


class NewsCreateForm(ModelForm):
    class Meta:
        model = News
        fields = ("image", "title", "content", "category")
