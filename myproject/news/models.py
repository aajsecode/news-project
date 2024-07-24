from django.db import models

# Create your models here.
"""
News
- Image
- Title
- TextField
- Created Date
- Update Date
- Author 
- Category
- Likes

Author
- Name
- Subtitle
- Bio
- Image

Category
- Name
- Description

Likes
- News
- User
"""


class Author(models.Model):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    bio = models.TextField(max_length=500)
    image = models.ImageField(upload_to="uploads/author_bio")

    def __str__(self):
        return self.name


class Category(models.Model):
    banner = models.ImageField(upload_to="uploads/category_banner")
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class News(models.Model):
    image = models.ImageField(upload_to="uploads/news_banner")
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    authored_by = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title
