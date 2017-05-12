from django.shortcuts import render
from .models import Article

# Create your views here.

def article_list(request):
    articles=Article.objects.all()
    return render(request, 'gblog/article_list.html', {'articles': articles})

