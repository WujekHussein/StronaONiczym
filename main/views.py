from django.shortcuts import render
from .models import Article, ArticleSeries
# Create your views here.
def home(request):
    matching_series = ArticleSeries.objects.all()

    return render(request,
                  'main/home.html',
                  {'objects' : matching_series})
def series(request, series: str):
    matching_series = Article.objects.filter(series__slug=series).all()

    return render(request,
                  'main/home.html',
                  {'objects': matching_series})
def article(request, series: str, article: str):
    matching_article = Article.objects.filter(series__slug=series, article_slug=article).first()

    return render(request,
                  "main/article.html",
                  {'object':matching_article})