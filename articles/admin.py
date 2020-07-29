from django.contrib import admin
from .models import User, Article, tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

# Register your models here.
admin.site.register(User)
admin.site.register(Article, ArticleAdmin)
admin.site.register(tags)