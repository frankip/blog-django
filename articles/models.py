from django.db import models

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
    post = models.TextField()
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/', null=True ,blank=True)

    @classmethod
    def get_search(cls, search_term):
        searched = cls.objects.filter(title__icontains = search_term)
        return searched

    @classmethod
    def get_single_article(cls, article_id):
        single_article = cls.objects.get(id = article_id)
        return single_article

    def __str__(self):
        return self.title