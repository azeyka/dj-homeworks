from django.shortcuts import render
from django.shortcuts import redirect

from .models import Article, Profile


def show_articles(request):
    return render(
        request,
        'articles.html',
        {
            'articles': Article.objects.all()
        }
    )

def show_article(request, id):
    user = Profile.objects.get(user=request.user)
    article = Article.objects.get(id=id)
    return render(
        request,
        'article.html',
        {
            'article': article,
            'user': user
        }
    )

def subscribe(request):
    user = Profile.objects.get(user=request.user)
    user.has_subscription = True
    user.save()

    return redirect(
        'article',
        id=request.GET.get('id')
    )
