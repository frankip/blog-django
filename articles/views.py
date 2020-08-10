from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime as dt
from .models import Article
from .forms import NewArticleForm

# Create your views here.

def welcome(request):
    date = dt.datetime.today()
    return render(request, 'welcome.html', {"date": date })


def create_article(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
        return redirect('articles')

    else:
        form = NewArticleForm()
    return render(request, 'new-article.html', {"form": form})

def view_articles(request):
    article_set = Article.objects.all()
    article = reversed(list(article_set))

    print('---articles', article)

    return render(request, 'articles.html', {"article": article})

def view_single_article(request, article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    context = {
        'id': article_id,
        "article": article,
    }
    return render(request, 'single_article.html', context)

def search_article(request):

    if 'article' in request.GET and request.GET.get('article'):
        search = request.GET.get('article')
        searched = Article.objects.filter(title__icontains = search)
        message = f"{searched}"
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
