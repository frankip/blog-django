from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Article

# Create your views here.

def welcome(request):
    date = dt.datetime.today()
    return render(request, 'welcome.html', {"date": date })


def view_articles(request):
    article = Article.objects.all()

    # print('---articles', article)

    return render(request, 'articles.html', {"article": article})


def get_single_article(request, article_id):
    single_article = Article.get_single_article(article_id)
    print('---single_article-->', single_article)
    context = {
        "single_article": single_article,
    }
    return render(request, 'get_single_article.html', context)

def search_article(request):

    if 'article' in request.GET and request.GET.get('article'):
        search = request.GET.get('article')
        searched = Article.get_search(search)
        context = {
            "searched" : searched,
        }
        return render(request, 'search.html', context)

    else:
        message = "no search terms"
        context = {
            "message": message,
        }
        return render(request, 'search.html', context)
