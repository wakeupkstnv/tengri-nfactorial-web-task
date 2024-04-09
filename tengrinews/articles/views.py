from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView

# Create your views here.
def articles_home(request):
    articles = Article.objects.order_by('-date')
    print(articles)
    return render(request, 'main/articles.html', {'article': articles})

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail_view.html'
    context_object_name = 'news'
    
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была не верной'
    
          
    form = ArticleForm()
    
    data = {
        'form': form,
        'error': error 
    }
    return render(request, 'main/create.html', data)