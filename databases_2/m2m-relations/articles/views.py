from django.views.generic import ListView

from articles.models import Article, Relationship


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        all_scopes = Relationship.objects.all().order_by('section__sections')
        articles = []
        for article in context['object_list']:
            scopes = []
            for scope in all_scopes.filter(article=article):
                if scope.is_main:
                    scopes.insert(0, scope)
                else:
                    scopes.append(scope)
            article.scopes = scopes
            articles.append(article)


        return {'object_list': articles}
