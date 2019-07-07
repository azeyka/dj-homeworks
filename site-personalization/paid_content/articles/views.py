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
    context = {}
    
    if not request.user.is_anonymous:
        user = Profile.objects.get(user=request.user)
        context['user'] = user
        
    article = Article.objects.get(id=id)
    context['article'] = article
    
    return render(
        request,
        'article.html',
        context
    )

def subscribe(request):
    user = Profile.objects.get(user=request.user)
    user.has_subscription = True
    user.save()

    return redirect(
        'article',
        id=request.GET.get('id')
    )
