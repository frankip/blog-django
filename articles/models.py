from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length =60)
    post = HTMLField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,  null=True)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/', null=True, blank=True)

    def __str__(self):
        return self.title